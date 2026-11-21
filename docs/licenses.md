# Licenses of the site's parts

This page lists the software and fonts that this site is built from and carries, each with its version, source and license.

The site loads nothing from the internet. Every part below is a file of the site folder, and the full text of each license is in the folder `assets/vendor/` beside the part it covers.

| Part | Version | Use | License | Source |
|---|---|---|---|---|
| MkDocs | 1.6.1 | builds the pages from their text | BSD-2-Clause | `pypi.org/project/mkdocs` |
| Material for MkDocs | 9.7.7 | the layout, the search and the icons of the pages | MIT | `pypi.org/project/mkdocs-material` |
| PyMdown Extensions | 13.1 | note boxes, code blocks, equations in the text | MIT | `pypi.org/project/pymdown-extensions` |
| KaTeX | 0.19.1 | draws the equations; its fonts are part of the site | MIT (fonts: SIL Open Font License 1.1) | `github.com/KaTeX/KaTeX`, release v0.19.1 |
| iframe-worker | 1.0.4 | lets the search work when the folder is opened from the disk | MIT | `registry.npmjs.org/iframe-worker` |
| Source Sans 3 | 3.052R | the text font | SIL Open Font License 1.1 | `github.com/adobe-fonts/source-sans`, release 3.052R |
| Source Code Pro | 2.042R-u / 1.062R-i / 1.026R-vf | the font of commands, paths and file names | SIL Open Font License 1.1 | `github.com/adobe-fonts/source-code-pro` |
| Liberation Sans | 2.1.5 | the letters of the figures | SIL Open Font License 1.1 | `github.com/liberationfonts/liberation-fonts`, release 2.1.5 |

The fonts are used as released, without any change.

The ground of the pages, contour lines of an invented terrain, is taken from nowhere: a script of the tutorial's sources, `tools/bg_contours.py`, draws it from a formula, one file for the light colors and one for the dark. It is part of the tutorial and comes under the tutorial's own license.
