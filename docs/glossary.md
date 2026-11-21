# Glossary

This page defines the terms of SWAT+ and of SWATrust used in this tutorial.

The terms of SWAT+ are given as its source code defines them; the file that holds each definition is given after the meaning, as "Defined in ...".

## The parts of a SWAT+ model

- **Basin**: The whole area of one model, drained through one outlet.
- **Hydrologic unit**: An area of land that drains to one point, with a number of its own, the hydrologic unit code (HUC). A HUC8 basin is a hydrologic unit with a code of eight digits, and a HUC8 model is the SWAT+ model of one such basin. The basin of this tutorial is the hydrologic unit 02070002.
- **Subbasin**: A part of the basin that drains to one point of the channel network.
- **HRU**: Hydrologic response unit, a share of a subbasin's area with one soil, one land use with its management, and one slope. SWAT+ computes the water balance of the land for each HRU.
- **Routing unit**: A group of HRUs whose water SWAT+ adds up and sends on as one. Defined in `rout_unit.def` and `rout_unit.ele`.
- **Channel**: A reach of the stream network. SWAT+ routes water, sediment and nutrients through it. Defined in `chandeg.con`.
- **Reservoir**: A water body on the channel network that stores water and releases it. Defined in `reservoir.con`.
- **Wetland**: A water body on the land of an HRU. Precipitation and irrigation on that HRU go to the wetland first. Defined in `wetland.wet`.
- **Aquifer**: The groundwater store under a part of the basin. It takes up recharge from the soil above and gives water to the channels. Defined in `aquifer.con`.
- **Point source**: A record of flows and loads that the model adds at one point. SWAT+ names such an object a recall. Defined in `recall.con` and `recall.rec`.
- **Outlet**: A point where the model records the water that passes. The basin outlet is the last point of the chain. Defined in `object.prt`.

## The water balance

Each term is a depth of water in mm, as the type `output_waterbal` of the SWAT+ source file `output_landscape_module.f90` defines it. In this list and the next, the name in brackets is the column of the output table.

- **Precipitation** (`precip`): Precipitation falling as rain and snow.
- **Snowfall** (`snofall`): Precipitation falling as snow, sleet or freezing rain.
- **Snowmelt** (`snomlt`): Melting snow or ice.
- **Surface runoff** (`surq_gen`): Surface runoff generated from the land.
- **Lateral flow** (`latq`): Flow through the soil to the side.
- **Tile flow** (`qtile`): Flow through subsurface drains that leaves the land.
- **Water yield** (`wateryld`): The sum of surface runoff, lateral flow and tile flow.
- **Percolation** (`perc`): Water that leaves the soil profile downward, into the vadose zone.
- **Evapotranspiration** (`et`): Actual evapotranspiration, that is, transpiration, evaporation from the soil and from the canopy, and the evaporation of the water of a wetland on the HRU.
- **Potential evapotranspiration** (`pet`): The evapotranspiration that the weather would allow.
- **Soil water** (`sw_ave`): The average water content of the soil profile.
- **Irrigation** (`irr`): Irrigation water applied.

The terms of an aquifer are those of the SWAT+ source file `aquifer_module.f90`.

- **Recharge** (`rchrg`): Water that enters the aquifer from other objects, in mm.
- **Aquifer flow** (`flo`): Flow from the aquifer to the side, in mm.
- **Seepage** (`seep`): Water that leaves the aquifer through its bottom, in mm.
- **Revap** (`revap`): Water that plants take up and that evaporates from the aquifer, in mm.
- **Depth to the water table** (`dep_wt`): The average depth from the surface to the water table, in m.

## Units

- **mm over the basin**: A volume of water divided by the land area of the model. One mm over 1 km² is 1,000 m³.
- **m³/s**: Flow. The record of an outlet holds the volume of each day in m³; the flow is that volume divided by 86,400, the seconds of a day.
- **`jday`**: The day of the year, from 1.

## Calibration and uncertainty analysis

In the formulas, `O` is the measured value of a day in a measured series, such as the daily flow at a gauge, `S` the simulated value of that day and `Ō` the mean of the measured values. Each sum runs over the days of the period that have a measured value.

- **NSE**: Nash-Sutcliffe efficiency. `NSE = 1 - Σ(O - S)² / Σ(O - Ō)²`.
- **KGE**: Kling-Gupta efficiency. `KGE = 1 - sqrt((r - 1)² + (α - 1)² + (β - 1)²)`. `r` is the linear correlation of the simulated and the measured series, `α` the standard deviation of the simulated series divided by that of the measured series, and `β` the mean of the simulated series divided by that of the measured series.
- **PBIAS**: Percent bias. `PBIAS = 100 · Σ(O - S) / ΣO`, in percent. A positive value means that the simulated series is lower than the measured series in the sum.
- **GLUE**: A method of uncertainty analysis. A set of parameter values is kept, and called behavioral, when its measure is at or above the threshold. The measure is the NSE or the KGE of the calibration period, computed from daily flows.
- **SUFI-2**: A method of uncertainty analysis that works in iterations. An iteration draws sets of parameter values from the range of each parameter by Latin hypercube sampling and makes one simulation with each set. The ranges of the next iteration are set around the best simulation of the iteration: the simulation with the highest KGE, or NSE, of the calibration period, computed from daily flows.
- **Band**: In the uncertainty analysis, a lower and an upper limit of the simulated flow for each day. GLUE forms it from the weighted 2.5 % and 97.5 % values of the behavioral sets, or from their weighted 5 % and 95 % values. SUFI-2 forms it from the same values of the simulations of an iteration, every simulation with the same weight. The page names the band of GLUE "95 % prediction limits", or "90 % prediction limits" at 5 % and 95 %, and the band of SUFI-2 at 2.5 % and 97.5 % "95PPU".
- **p-factor**: The share of the days with a measured value on which the measured value lies inside the band, the two limits included.
- **r-factor**: The mean width of the band on the days with a measured value, divided by the standard deviation of the measured values on those days.

[Calibrate and validate](calibrate.md) and [Uncertainty analysis](uncertainty.md) use these terms.

## Files and tables

- **Model folder**: The folder of text files that is one SWAT+ model.
- **`file.cio`**: The file of a model that lists its other files. A folder with a `file.cio` is a SWAT+ model for SWATrust.
- **`TxtInOut`**: The name SWATrust gives its copy of a model in the run folder.
- **Output table**: A text file that the engine writes, with one line for each object and step.
- **Step**: How often a table has a line. The steps are day, month (`mon`), year (`yr`) and the average year (`aa`).
- **Record**: The daily file of one object that the model asks for in `object.prt`. In the model of this tutorial the records at outlets are named `<number>_con.out` and the records of channels `comid_<number>.out`.
- **Warm-up**: The years at the start of a run that are simulated but not written to the tables.

[File reference](files.md) describes each of these files.

## SWATrust

- **Launcher**: The program that shows the SWATrust page in your browser and starts the runs.
- **Engine**: The program that runs a SWAT+ model and writes its output tables.
- **Run**: One start of the engine on one or more basins, with its period and its choice of tables.
- **Runs folder**: The folder that keeps every run.
- **Copy of the model**: The copy of a model that SWATrust makes for a run. A run writes its settings into the copy and nothing into the model folder.
- **Thread**: One of the lines of work that a processor carries out at the same time. The engine can use several threads inside one basin, and the launcher can run several basins at once. The number of threads is a setting of the run. It changes no input file.
