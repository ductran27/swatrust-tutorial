#!/usr/bin/env python3
"""Draw the ground pattern of the tutorial's pages: contour lines of an invented terrain.

Usage: python3 bg_contours.py <site source folder>
Writes docs/assets/img/ground_light.svg and docs/assets/img/ground_dark.svg, one for each color scheme
of the site. The terrain is a sum of sine waves with whole numbers of waves across the tile, so the tile
repeats without a seam in both directions. It is a formula, not a map: no real place is drawn.
The site shows the lines at the right side of the window only, fading out towards the column of text
(site.css), so the body text, the tables and the list of chapters stand on plain ground and only the list
"Table of contents" at the right stands over lines. The script prints, for each scheme, the contrast of
that list's text against the plain ground and against an index line at the strength it has under the
list (at most SIDE_STRENGTH of its own, by the fade of site.css), the worst place,
so that the loss can be read as a number, and the contrast of the body text on its plain ground.
"""
import colorsys
import math
import os
import random
import sys

W, H, CELL = 1200, 840, 6          # the tile and the grid step, in px
NX, NY = W // CELL, H // CELL
LEVELS = 15                        # lines between the lowest and the highest ground
INDEX_EVERY = 5                    # every fifth line is drawn a little stronger, as on a map
SEED = 20261116
SIDE_STRENGTH = 0.45               # the most a line keeps under the list at the right (the fade of site.css)

# scheme: (file, line color, opacity of a line, opacity of an index line, ground, body text, text of the list at the right)
SCHEMES = {
    "light": ("ground_light.svg", "#12589f", 0.12, 0.19, (255, 255, 255), (0x14, 0x18, 0x1C), (0x14, 0x18, 0x1C)),
    "dark": ("ground_dark.svg", "#a9cdee", 0.11, 0.18, None, None, None),   # ground and texts: see dark_colors
}


def dark_colors(hue=212):
    """The dark scheme's ground, as the theme computes it from the hue set in site.css, and its body text and
    list text, which site.css sets to white for every text of that scheme."""
    def hsl(h, s, l):
        r, g, b = colorsys.hls_to_rgb(h / 360.0, l, s)
        return (r * 255, g * 255, b * 255)
    ground = hsl(hue, 0.15, 0.14)
    text = (255.0, 255.0, 255.0)
    side = text
    return ground, text, side


def terrain():
    rnd = random.Random(SEED)
    waves = []
    for m in range(-3, 4):
        for n in range(0, 4):
            k2 = m * m + n * n
            if k2 == 0 or k2 > 10 or (n == 0 and m < 0):
                continue
            waves.append((m, n, rnd.uniform(0.5, 1.0) / k2 ** 1.15, rnd.uniform(0, 2 * math.pi)))
    return [[sum(a * math.cos(2 * math.pi * (m * i / NX + n * j / NY) + p) for m, n, a, p in waves)
             for i in range(NX + 1)] for j in range(NY + 1)]


def contour(z, level):
    """The lines of one height, as lists of points; a line that leaves the tile goes on in the next tile."""
    pts, segs = {}, []

    def cross(key, a, b, pa, pb):
        t = (level - a) / (b - a)
        pts[key] = (pa[0] + t * (pb[0] - pa[0]), pa[1] + t * (pb[1] - pa[1]))
        return key

    for j in range(NY):
        for i in range(NX):
            a, b, c, d = z[j][i], z[j][i + 1], z[j + 1][i + 1], z[j + 1][i]   # corners, clockwise from top left
            ua, ub, uc, ud = a > level, b > level, c > level, d > level
            if ua == ub == uc == ud:
                continue
            x0, y0, x1, y1 = i * CELL, j * CELL, (i + 1) * CELL, (j + 1) * CELL
            top = cross(("h", i, j), a, b, (x0, y0), (x1, y0)) if ua != ub else None
            right = cross(("v", i + 1, j), b, c, (x1, y0), (x1, y1)) if ub != uc else None
            bottom = cross(("h", i, j + 1), d, c, (x0, y1), (x1, y1)) if ud != uc else None
            left = cross(("v", i, j), a, d, (x0, y0), (x0, y1)) if ua != ud else None
            keys = [k for k in (top, right, bottom, left) if k]
            if len(keys) == 2:
                segs.append((keys[0], keys[1]))
            elif ((a + b + c + d) / 4 > level) == ua:    # a saddle whose middle joins the corners a and c
                segs += [(top, right), (bottom, left)]
            else:
                segs += [(top, left), (bottom, right)]
    at = {}
    for s, (k1, k2) in enumerate(segs):
        at.setdefault(k1, []).append(s)
        at.setdefault(k2, []).append(s)
    used = [False] * len(segs)

    def run(k):
        line = [pts[k]]
        while True:
            free = [s for s in at[k] if not used[s]]
            if not free:
                return line
            used[free[0]] = True
            k = segs[free[0]][1] if segs[free[0]][0] == k else segs[free[0]][0]
            line.append(pts[k])

    lines = []
    for k in at:                                   # lines that end at the tile's edge
        if len(at[k]) == 1 and not used[at[k][0]]:
            lines.append(run(k))
    for k in at:                                   # closed lines
        if any(not used[s] for s in at[k]):
            lines.append(run(k))
    return lines


def path(lines):
    def n(v):
        return ("%.1f" % v).rstrip("0").rstrip(".")
    return "".join("M" + " ".join(n(x) + "," + n(y) for x, y in line) for line in lines)


def luminance(rgb):
    def lin(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(c1, c2):
    a, b = sorted((luminance(c1), luminance(c2)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    out = os.path.join(os.path.abspath(sys.argv[1]), "docs", "assets", "img")
    z = terrain()
    lo, hi = min(map(min, z)), max(map(max, z))
    thin, index = [], []
    for k in range(1, LEVELS + 1):
        lines = contour(z, lo + (hi - lo) * k / (LEVELS + 1))
        (index if k % INDEX_EVERY == 0 else thin).extend(lines)
    for name, (fname, stroke, o_thin, o_index, ground, text, side) in SCHEMES.items():
        if ground is None:
            ground, text, side = dark_colors()
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
               '<!-- contour lines of an invented terrain (a sum of sine waves), drawn by tools/bg_contours.py; '
               'not a map of a real place -->\n'
               f'<path fill="none" stroke="{stroke}" stroke-opacity="{o_thin}" stroke-width="1" d="{path(thin)}"/>\n'
               f'<path fill="none" stroke="{stroke}" stroke-opacity="{o_index}" stroke-width="1.2" '
               f'd="{path(index)}"/>\n</svg>\n')
        with open(os.path.join(out, fname), "w", encoding="utf-8") as f:
            f.write(svg)
        s = tuple(int(stroke[i:i + 2], 16) for i in (1, 3, 5))
        o_side = o_index * SIDE_STRENGTH
        on_line = tuple(o_side * a + (1 - o_side) * g for a, g in zip(s, ground))
        print(f"{name}: {fname} {len(svg) // 1024} KiB, {len(thin) + len(index)} lines; contrast of the body text "
              f"on its plain ground {ratio(text, ground):.2f}; of the list at the right on the plain ground "
              f"{ratio(side, ground):.2f}, on an index line under that list {ratio(side, on_line):.2f}")


if __name__ == "__main__":
    main()
