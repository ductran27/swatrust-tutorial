# SWATrust tutorial

The sources of the SWATrust tutorial: step-by-step chapters for running SWAT+ models with SWATrust.

## Build the site

The site is built with MkDocs. With Python 3.13:

```
python -m pip install -r requirements.txt
python -m mkdocs build --strict
```

The pages are written to the folder `site/`. Open `site/index.html` in a browser: the folder works from
the disk, and no page loads anything from the internet. Fonts, the math renderer and the scripts are
files of the site (`docs/assets/vendor/`, each with its license).

## What is where

| Path | Holds |
|---|---|
| `mkdocs.yml` | the configuration of the site and the order of the chapters |
| `docs/` | the chapters (`.md`) and their files: styles, scripts, pictures, videos, fonts |
| `include/` | the blocks that the chapters include: figures, pictures, videos |
| `overrides/` | two parts of the theme that the site replaces |
| `tools/bg_contours.py` | the script that draws the ground pattern of the pages |
| `requirements.txt`, `.readthedocs.yaml` | the pinned packages and the build on Read the Docs |
| `LICENSE` | the license of the tutorial and its videos |

## License

© 2026 Duc Tran. This tutorial and its videos are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/.

The licenses of the parts the site carries are listed on its page "Licenses of the site's parts".
