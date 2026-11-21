# Find the outputs

This page shows where SWATrust writes the output tables of a run, how the files are named, and how to move a run or remove an old one.

The run of this page is the run of [Run streamflow](run-streamflow.md): the basin 02070002, 2000 to 2015, with a warm-up of three years.

## From the Results view to the folder

1. Click **Results** in the left column.
2. In the box **Basin**, pick the basin. The box lists the basins that have results, each from its newest run.
3. Look at **Output folders**, at the foot of the first column. It has one row for each basin that has results, with the name of the basin and the button **Open output folder**. The row of a basin stands for its newest run, so a basin that ran twice has one row, and its earlier run has none.

--8<-- "include/shots/s07_1_files.html"

The folder of the run of this page holds these kinds of files.

| Kind of file | Files |
|---|---|
| Flow at 37 outlets, daily | 37 |
| Flow in 24 channels, daily | 24 |
| Entire-basin water balance | 4 |
| Entire-basin nutrient balance | 3 |
| Entire-basin sediment and nutrients | 3 |
| Entire-basin plants and weather | 3 |
| Crop yields, entire basin | 2 |
| HRU water balance | 3 |
| HRU sediment and nutrients | 2 |
| HRU plants and weather | 2 |
| Aquifers | 2 |
| Reservoirs | 2 |
| Wetlands | 2 |
| Channels | 5 |
| Channel budgets | 3 |
| Crop yields | 1 |
| Carbon | 4 |
| Files for SWIFT | 62 |
| Notes and checks of the run | 11 |
| Other files | 6 |

The folder `out` of the run holds 119 files and the folder `SWIFT`:

- 37 files whose names end in `_con.out`, such as `020700020101_con.out`;
- 24 files named `comid_<number>.out`, such as `comid_14362658.out`;
- 47 tables whose names end in `.txt`, from `aquifer_aa.txt` to `wetland_yr.txt`;
- 11 more files: `area_calc.out`, `checker.out`, `co2.out`, `diagnostics.out`, `erosion.out`, `files_out.out`, `flow_duration_curve.out`, `fort.2103`, `fort.7777`, `simulation.out` and `success.fin`.

The page draws from some of these files. It does not show a table as a table: you open the files with your own programs. [Read the results](read-results.md) shows how.

## The folder of a run

Every run has a folder of its own in the runs folder. The name of the folder is the date and the time of the start.

```text
~/SWATrust/runs/
    run_<date>_<time>/
        basins.csv
        run.json
        02070002/
            TxtInOut/
            out/
            engine_main.args
            engine_main.err
            engine_main.out
            engine_main.pid
```

| Item | What it is |
|---|---|
| `basins.csv` | one line for each basin of the run |
| `run.json` | the settings and the state of the run, for SWATrust itself |
| `02070002/` | one folder for each basin, named after its model |
| `TxtInOut/` | the copy of the model that the engine ran |
| `out/` | everything the engine wrote |
| `engine_main.args`, `.err`, `.out`, `.pid` | the engine's command line, what it printed, and its process number |

The model folder that you gave SWATrust is not in this list, and the run writes nothing into it. The run was made on the copy in `TxtInOut/`, so the copy shows the years and the tables that the run had.

## The output tables

The folder `out/` holds one text file for each output table and each step that the run writes.

```text
basin_wb_day.txt
basin_wb_mon.txt
basin_wb_yr.txt
basin_wb_aa.txt
```

The first part of the name is the table. The last part is the step: `day`, `mon` for month, `yr` for year, and `aa` for the average year.

With the ticks of [Run streamflow](run-streamflow.md), the run of this page writes 16 tables in 38 files.

| Tables | What they hold | Steps in this run |
|---|---|---|
| `basin_wb` | the water balance of the entire basin | day, month, year, average year |
| `hru_wb` | the water balance of each HRU | month, year, average year |
| `basin_nb` | the nutrient balance of the entire basin | month, year, average year |
| `basin_ls` | sediment and nutrients that leave the land, entire basin | month, year, average year |
| `hru_ls` | sediment and nutrients that leave the land, each HRU | year, average year |
| `basin_pw` | plants and weather, entire basin | month, year, average year |
| `hru_pw` | plants and weather, each HRU | year, average year |
| `channel_sd` | the channels: water, sediment and nutrients | day, year, average year |
| `sd_chanbud`, `channel_sdmorph` | the budgets and the shape of each channel | year, average year |
| `aquifer` | the aquifers | year, average year |
| `reservoir`, `wetland` | the reservoirs and the wetlands | year, average year |
| `basin_crop_yld` | crop yields, entire basin | year, average year |
| `crop_yld` | crop yields | average year |
| `hru_nut_carb_gl` | head lines only | year, average year |

Two of these files can surprise a reader.

- The two files of `hru_nut_carb_gl` hold head lines and no values.
- `channel_sd_day.txt` holds head lines only unless the box of the row **Every channel** in the column **Day** is ticked.

## The record of an outlet

The model asks for the daily record of single objects in its file `object.prt`. The engine writes each record as one file in `out/`, under the name the model gives it. In the model of this page the 37 records at outlets are named `<number>_con.out`, and the 24 records at channels are named `comid_<number>.out`. These are the first two kinds of the table above.

The record of the basin outlet is `020700020803_con.out`. [Run streamflow](run-streamflow.md#read-the-flow-at-the-outlet) reads it, and [File reference](files.md#the-records-of-objectprt) gives its columns and units.

## Other files in `out/`

The engine also writes the notes of the run that SWAT+ writes. You do not need them for the chapters of this tutorial. They are text files written on every run. They tell what was read from the model and whether the run reached its end, so look there first when a run stops early.

| File | What it is |
|---|---|
| `simulation.out` | the log of the run |
| `success.fin` | written when the run reached its last day |
| `files_out.out` | the list of the output tables that the run wrote |
| `diagnostics.out`, `checker.out`, `area_calc.out`, `erosion.out`, `co2.out`, `flow_duration_curve.out` | notes and summaries of SWAT+ on the model and the run |
| `fort.7777`, `fort.2103` | two files that carry a number in place of a name |
| `SWIFT/` | a folder of 62 files |

The file `success.fin` holds the line "Execution successfully completed". The folder `SWIFT/` holds input files for the SWIFT model, written with each run. The SWAT+ results do not need them.

## Move a run or remove an old one

A run is its folder. To keep a run somewhere else, copy the folder `run_<date>_<time>`.

Move or remove a folder only while no run is going.

Started with `--runs` and a folder, the launcher writes its runs, and the lists of models and runs, in that folder. [Install and start SWATrust](install.md#choose-where-swatrust-keeps-its-runs) shows the line.

## Video

--8<-- "include/slots/07_outputs.html"

## Next

- [Read the results](read-results.md) reads the tables of the water balance.
- [File reference](files.md) lists the head lines and the columns.
