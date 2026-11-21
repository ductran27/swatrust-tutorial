# File reference

This page describes the files of a SWAT+ model that SWATrust reads and the files it writes for a run.

The lines shown are those of the basin 02070002 (North Branch Potomac), in the run of [Run streamflow](run-streamflow.md): 2000 to 2015 with a warm-up of three years.
## The model folder

A SWAT+ model is one folder of text files. The file `file.cio` lists them. SWAT+ reads `file.cio` in the routine `readcio_read`: a title line, then one line for each group of files. A line starts with the name of the group and then names the files of that group. The word `null` stands for a file the model does not have.

The model of this page has 25 groups and five lines for the folders of weather files. This tutorial works with four of the groups.

| Group in `file.cio` | Files named in this model | What they hold |
|---|---|---|
| `SIMULATION` | `time.sim`, `print.prt`, `object.prt`, `object.cnt`, `constituents.cs` | the period, the output tables to write, single-object records, object counts |
| `CLIMATE` | `weather-sta.cli`, `pcp.cli`, `tmp.cli`, `slr.cli`, `hmd.cli`, `wnd.cli` and others | the weather stations and the lists of the weather files |
| `CONNECT` | `hru.con`, `rout_unit.con`, `aquifer.con`, `chandeg.con`, `reservoir.con`, `recall.con`, `outlet.con` and others | which object sends its water to which |
| `CHG` | `cal_parms.cal`, `calibration.cal` and seven `.sft` files | the parameters that can be changed and the changes to apply |

The other groups are `BASIN`, `CHANNEL`, `RESERVOIR`, `ROUT_UNIT`, `HRU`, `EXCO`, `RECALL`, `DR`, `AQUIFER`, `HERD`, `WATER_RIGHTS`, `LINK`, `HYDROLOGY`, `STRUCTURAL`, `HRU_PARM_DB`, `OPS`, `LUM`, `INIT`, `SOILS`, `DECISION_TABLE` and `REGIONS`.

## What SWATrust writes into its copy of the model

A run writes nothing into the model folder you give it. For each run SWATrust copies the model into the run folder, as `TxtInOut`, and writes the choices of the run into the copy. On a disk that keeps letter case, where the model names a file in other letter case than the folder holds it, the copy also holds that file under the name the model asks for ([Messages and troubleshooting](troubleshooting.md#a-name-with-other-letter-case)). The engine then runs the copy.

### `time.sim`: the years

```text
 DAY_START YRC_START DAY_END YRC_END  STEP
         0      2000       0    2015     0
```

`YRC_START` and `YRC_END` are the first and the last year of the run. SWAT+ reads the line in the routine `time_read`. It takes a `DAY_START` of 0 as day 1 of the year, and a `STEP` of 0 as one step a day.

### `print.prt`: the warm-up and the output tables

```text
 N_Yrs_SKIP   JD_START  YRC_START     JD_END    YRC_END   INTERVAL
          3          0          0          0          0          1
 aa_int_cnt
          0
 CSVOUT DBOUT CDFOUT
      n     n      n
CROPYLD MGTOUT HYDCON FDCOUT
    a     n    n      y
       OBJECTS     DAILY   MONTHLY    YEARLY     AVANN
      basin_wb         y         y         y         y
      basin_nb         n         y         y         y
```

`N_Yrs_SKIP` is the warm-up: the number of years at the start of the run that are simulated but not written to the tables. After the four head blocks the file has one line for each output table, with `y` or `n` for the daily, the monthly, the yearly and the average-year table. These letters are the ticks of the list **Output tables** in Set-up. SWAT+ reads the file in the routine `basin_print_codes_read`.

### `object.prt`: the record of a single object

```text
          ID  OBJ_TYP  OBJ_TYP_NO  HYD_TYP              FILENAME
           1      out           1      tot  020700020101_con.out
           2      out           2      tot  020700020102_con.out
```

Each line asks for the daily record of one object: the ID of the line (1, 2, 3 and so on, in order), the kind of object, its number among the objects of that kind, the kind of hydrograph, and the name of the file to write. SWAT+ reads the file in the routine `object_read_output`. The model of this page asks for 61 records, all with the hydrograph `tot`: 37 at outlets (`out`), named `<number>_con.out`, and 24 of channels (`sdc`), named `comid_<number>.out`. The daily flow of [Run streamflow](run-streamflow.md) is drawn from one of them.

### `calibration.cal`: changes to parameters

```text
NAME                  CHG_TYPE             VAL               CONDS  LYR1   LYR2  YEAR1 YEAR2  DAY1  DAY2  OBJ_TOT
alpha                   absval        0.767087                   0     0      0      0     0     0     0        0
flo_min                 pctchg       91.757609                   0     0      0      0     0     0     0        0
```

The first line of the file is a title and the second the number of changes. Each change names a parameter, the kind of change and a value. The columns after the value give the number of conditions, a first and a last layer, year and day, and a count of elements. A change whose `CONDS` is above 0 is followed by one line for each condition. SWAT+ reads the file in the routine `cal_parmchg_read` and applies each change in the function `chg_par`.

| `CHG_TYPE` | New value of the parameter |
|---|---|
| `absval` | the value given |
| `abschg` | the current value plus the value given |
| `pctchg` | the current value changed by the given percent |
| `relchg` | the current value times one plus the value given |

SWAT+ then holds the result within the limits of the parameter, the lowest and the highest value that `cal_parms.cal` gives for it.

The model of this page comes with a `calibration.cal` of 188 changes, 131 of them with one condition. [Calibrate and validate](calibrate.md) shows how SWATrust writes a new one.

## The runs folder

SWATrust keeps every run in the runs folder, `~/SWATrust/runs` unless you chose another place.

```text
~/SWATrust/runs/
    models.json
    history.json
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
| `models.json`, `history.json` | lists of your model folders and of earlier runs, for SWATrust itself |
| `run_<date>_<time>/` | one run; the name is the date and time of its start |
| `basins.csv` | one line for each basin of the run |
| `run.json` | the settings of the run, for SWATrust itself |
| `02070002/` | one folder for each basin of the run, named after the model |
| `TxtInOut/` | the copy of the model that the engine ran |
| `out/` | everything the engine wrote |
| `engine_main.args`, `.err`, `.out` | the engine's command line and what it printed |
| `engine_main.pid` | the number of the engine's process, for SWATrust itself |

A line of `basins.csv` gives the state, the years, the warm-up, the threads asked and the threads used, the run time, the peak memory, the sizes, and whether missing point-source files were read as zero inflow.

In `basins.csv`, "Threads asked" is the number set on the Run page, and "Threads used" is the number the engine ran on.

## The output tables

The folder `out/` holds the output tables as text files. A table is written once for each step that is ticked, and the step is the end of the file's name.

| End of the name | Step |
|---|---|
| `_day.txt` | one line for each object and day |
| `_mon.txt` | one line for each object and month |
| `_yr.txt` | one line for each object and year |
| `_aa.txt` | one line for each object, the average year |

Each table starts with three head lines: a title, the names of the columns and their units. The two tables of crop yields have head lines of another form. The first seven columns are the same in every other table: `jday`, `mon`, `day`, `yr`, `unit`, `gis_id` and `name`. A column without a unit has a blank in the units line, so a unit belongs to the name that stands above it, not to the word with the same count in the line.

In the four basin tables, `basin_wb`, `basin_nb`, `basin_ls` and `basin_pw`, a line has fewer values than the head has names. The names `plant_cov` and `mgt_ops` at the end of the head have no values under them, and neither has `percn`, which follows them in `basin_ls`. The line of `basin_wb_aa.txt` is the exception: it ends with words that belong to no column. The tables of the HRUs have a value under every name.

| Table | What it holds |
|---|---|
| `basin_wb`, `hru_wb` | the water balance of the entire basin and of each HRU |
| `basin_nb` | the nutrient balance of the entire basin |
| `basin_ls`, `hru_ls` | sediment and nutrients that leave the land |
| `basin_pw`, `hru_pw` | plants and weather |
| `channel_sd` | storage, inflow and outflow of water, sediment and nutrients of every channel |
| `sd_chanbud` | the sediment and nutrient budget of every channel |
| `channel_sdmorph` | flow, sediment, and the width, depth and slope of every channel |
| `aquifer` | storage, recharge and flow of every aquifer |
| `reservoir`, `wetland`, `basin_res` | area, storage, inflow and outflow: reservoirs, wetlands, all reservoirs of the basin |
| `crop_yld`, `basin_crop_yld` | crop yields |
| `hru_nut_carb_gl` | head lines only: SWAT+ writes no values into this table |

Without the tick of the Day box of `channel_sd`, `channel_sd_day.txt` is still written, with head lines only.

### The records of `object.prt`

A record file has one head line and no units line. Each line after it is one day. The head line reads `name type`, but the values are written type first: the column headed `name` holds the kind of the object, `outlet` at an outlet, and the column headed `type` holds the name of the object.

A record holds every day of the run, the warm-up years included.

The columns after `type` are those of the type `hyd_output` in the SWAT+ source file `hydrograph_module.f90`. Each holds the amount of one day, except the last, which is a temperature.

| Column | Holds | Unit |
|---|---|---|
| `flo` | volume of water | m³ |
| `sed` | sediment | metric tons |
| `orgn`, `no3` | organic nitrogen, nitrate | kg N |
| `sedp`, `solp` | organic phosphorus, soluble phosphorus | kg P |
| `chla`, `cbod`, `dox` | chlorophyll-a, carbonaceous biological oxygen demand, dissolved oxygen | kg |
| `nh3`, `no2` | ammonia, nitrite | kg N |
| `san`, `sil`, `cla`, `sag`, `lag`, `grv` | sediment by size class: sand, silt, clay, small aggregates, large aggregates, gravel | metric tons |
| the last column, headed `null` | temperature | °C |

## Next

- [Find the outputs](outputs.md) leads from the Results view to these files.
- [Read the results](read-results.md) reads the tables of the water balance.
