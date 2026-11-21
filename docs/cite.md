# Cite, license and versions

This page says how to cite SWATrust, under which license each of its parts is released, and where your copy shows its version.

## Cite SWATrust

To cite SWATrust, name the program, its version and its author:

Tran, D. (2026). SWATrust (version 1.0.0) [Computer software].

[Versions](#versions) shows where your copy says its version.

A result made with one of the HUC8 models of the published data set cites the data set as well.

Tran, D. (2026). SWATrust: SWAT+ input files for HUC8 basins of the conterminous United States [Dataset]. figshare. https://doi.org/10.6084/m9.figshare.35018494

A study that runs SWAT+ with SWATrust cites SWAT+ as well (Bieger et al., 2017).

Bieger, K., Arnold, J.G., Rathjens, H., White, M.J., Bosch, D.D., Allen, P.M., Volk, M., Srinivasan, R., 2017. Introduction to SWAT+, a completely restructured version of the Soil and Water Assessment Tool. Journal of the American Water Resources Association 53 (1), 115-130.

## License

| Part | License |
|---|---|
| The code of SWATrust: the launcher and the engine | MIT License |
| This tutorial and its videos | CC BY 4.0 |
| The HUC8 models of the published data set | CC BY 4.0, the license of the data set |

Under the MIT License you may use, copy, change and pass on the code, and sell copies of it. Every copy keeps the copyright line and the text of the license. The code comes without a warranty.

The text of the license is the file `LICENSE` in the SWATrust folder. Its copyright line reads as follows.

```text
Copyright (c) 2026 Duc Tran
```

Every page of the tutorial carries the line "© 2026 Duc Tran. This tutorial and its videos are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/." at its foot. The line covers the videos too. They are not under the MIT License. Under CC BY 4.0 you may copy, change and pass on the tutorial and its videos if you name the author, give the address of the license and say what you changed.

The maps of the page are drawn from the Watershed Boundary Dataset (the outlines of the hydrologic units), NHDPlus V2.1 (streams and water bodies) and GMTED2010 (elevation).

The measured values that the Calibration page downloads come from the U.S. Geological Survey (USGS).

The software and the fonts that these pages are built from have their own licenses. [Licenses of the site's parts](licenses.md) lists them.

## Versions

This tutorial was written for SWATrust 1.0.0. SWATrust 1.0.0 follows the SWAT+ source code of 29 April 2026, which builds on SWAT+ revision 61.0.2.11.

Your copy shows its version in two places.

| Where | What you see |
|---|---|
| The terminal, when the launcher starts | the first line, `SWATrust launcher <version>` |
| The terminal, after the line below | `swatrust <version>`; the launcher then stops |

```text
./swatrust --version
```

A chapter of this tutorial whose steps were done on SWATrust ends with a line that names the version, the package and the day of the check.
