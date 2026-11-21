# Get to know SWATrust

This page says what SWATrust is and what the four views of its page do.

## What SWATrust is

SWATrust is a port of SWAT+ to the Rust language, with a launcher that runs in your browser. SWAT+ is the Soil and Water Assessment Tool Plus, a watershed model written in Fortran. SWATrust reads the input files of a SWAT+ model, the files of its `TxtInOut` folder, and writes output tables in the formats of SWAT+.

SWATrust has two programs. The engine, `swatrs`, simulates a model. The launcher, `swatrust`, is a page in the web browser of your computer, on which you choose models, run them, look at the results and calibrate.

This version of SWATrust does not include every part of SWAT+. A model that uses a part it does not include is not run, and the Set-up page says so.

## What SWAT+ is

The film below introduces SWAT+ for a reader who has not used it: what the model simulates, the parts a SWAT+ model is made of, and the tables it writes.

--8<-- "include/slots/00_swatplus_intro.html"

## The four views of the page

The left column of the page names four views.

| View | What you do there | Chapters |
|---|---|---|
| **Set-up** | choose the models, the years of the run and the output tables | [Get a model](models.md), [Change inputs](change-inputs.md) |
| **Run** | start a run, watch it and stop it | [Run streamflow](run-streamflow.md), [Run several basins](run-many.md) |
| **Results** | see the flow, water balance and output folder of a run | [Read the results](read-results.md), [Find the outputs](outputs.md) |
| **Calibration** | calibrate a model on measured flow and analyze its uncertainty | [Calibrate and validate](calibrate.md), [Uncertainty analysis](uncertainty.md) |

--8<-- "include/shots/s01_1_views.html"

## Video

--8<-- "include/slots/01_about.html"

## Next

- [Download](download.md) says what to download for the tutorial.
- [Quick start](quick-start.md) runs one basin, 02070002 (North Branch Potomac).