# Change inputs

This page shows what SWATrust lets you set for a run, and where each setting goes.

## What SWATrust sets

SWATrust runs a copy of the model. A run writes your settings into the copy and nothing into the folder of the model.

| Setting | Where you set it in **Set-up** | File of the copy that holds it |
|---|---|---|
| The years of the run | **First year**, **Last year** | `time.sim` |
| The warm-up | **Warm-up** | `print.prt` |
| The output tables | **Output tables** | `print.prt` |
| The calibrated values | **Calibrated values** | `calibration.cal` |

## Change the years and the warm-up

1. In **Set-up**, click **Clear choice** and tick the model, so that it is the only model chosen.
2. Type the first year and press ++enter++. Do the same for the last year.
3. Type the number of warm-up years and press ++enter++.

The line under the three boxes says how many years run and for which years the model holds weather. For the years 2010 to 2013 and a warm-up of 1, it reads "4 years, the first as warm-up. Weather: 1981 to 2025." The warm-up years are simulated, but not written to the tables.

A period that the model cannot run is refused in the same line, with the years to choose from.

- A first year before the weather of the model: "The first year, 1970, is before the model's weather, which starts in 1981. Choose a first year from 1981 to 2015."
- A last year before the first year: "The last year, 2005, is before the first year, 2010. Choose a last year from 2010 to 2025."
- A warm-up as long as the run: "The warm-up, 4 years, leaves no year to print: the run simulates 4 years. Choose a warm-up from 0 to 3."

**Continue to Run** still works while a period is refused. **Run** then repeats the line under **Checks before the run**, and the run does not start: the page says "To start: settle each line marked with a red cross above."

## Choose the output tables

The column **Output tables** has one row for each table and one box for each time step: **Day**, **Mon**, **Year** and **Avg**, the average year.

1. Tick a box to write that table at that time step.
2. Clear a box to leave the table out.

The page opens with the ticks of the model's own tables. For the basin 02070002, SWATrust adds one tick and says so under the list: "SWATrust ticked 1 table for the Results view." The tick is the daily water balance of the entire basin, from which **Results** draws its charts.

Some rows have boxes that cannot be ticked. The **i** of the column says of them: "A table with locked boxes is not written by this version."

--8<-- "include/shots/s14_1_tables.html"

A tick changes the files of the run. With the box **Mon** of the row **Aquifers** ticked, the run writes `aquifer_mon.txt`. With the box **Mon** of the row **Plants and weather** of the entire basin cleared, the run does not write `basin_pw_mon.txt`. [Find the outputs](outputs.md) says which file each row writes.

Daily tables of every HRU or every channel are large. Before a run starts, **Run** gives the disk space that the run needs, under **Checks before the run**.

## Choose the calibrated values

Under **Calibrated values**, the page names the file of calibrated values that the run applies. For a model with a file `calibration.cal` of its own, the line reads "the model's own" and gives the path of the file. For a model without one, it reads "the model has none".

To run with another file:

1. Click **Choose**. The dialog "Choose a calibration.cal file" opens on the folder of the model.
2. Go to the file, and click it.
3. Click **Use this file**.

The line now reads "another file, copied into the run", and a button **Own** stands beside **Choose**. **Own** goes back to the model's own file. The chosen file is copied into the copy of the run, and nothing is written into the folder of the model.

[Calibrate and validate](calibrate.md) writes such a file of fitted values.

## Change another input

To change any other input, change it in a copy of the model with the tools that you built the model with, and add the copy as [Run your own model](own-model.md) describes.

## Video

--8<-- "include/slots/14_change_inputs.html"

## Next

- [File reference](files.md) describes the input files that SWATrust sets.
- [Messages and troubleshooting](troubleshooting.md) lists what the page says when a setting is refused.
