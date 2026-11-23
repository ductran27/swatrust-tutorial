# Run streamflow

This page shows how to set the period of a run, start it, and read the daily flow at the basin outlet and the water balance.

You run the North Branch Potomac model (02070002) from 2000 to 2015 with a warm-up of three years. At the end you have the simulated daily flow at the outlet for 2003 to 2015, on the page and as a file, and the water balance of the basin by day, month and year.

!!! note "Before you start"
    SWATrust is started and the basin 02070002 is in the list of models, as at the end of the [Quick start](quick-start.md). The steps of this page were done on Linux.

## How the model gets to the flow at the outlet

A SWAT+ model divides the basin into hydrologic response units (HRUs): shares of a subbasin's area, each with one soil, one land use with its management, and one slope. Each day the model simulates the water balance of every HRU. Routing units collect the water of their HRUs, the channels carry it downstream through the reservoirs, and the aquifers and the point sources add theirs. The flow of this page is the water that passes the last point of that chain, the basin outlet.

--8<-- "include/fig/fig06_parts.html"

In the model of this page the chain has 895 HRUs, 74 routing units, 1,658 channels, 37 aquifers, 85 reservoirs and 37 point sources over 3,531 km².

The land phase of SWAT+ rests on the water balance equation of SWAT (Neitsch et al., 2011, section 0.2.1):

\[
SW_t = SW_0 + \sum_{i=1}^{t} \left( R_{day} - Q_{surf} - E_a - w_{seep} - Q_{gw} \right)
\]

where \(SW_t\) is the soil water at the end of day \(t\) (mm), \(SW_0\) is the soil water at the start (mm), \(R_{day}\) is the precipitation of day \(i\) (mm), \(Q_{surf}\) is the surface runoff (mm), \(E_a\) is the evapotranspiration (mm), \(w_{seep}\) is the water that passes from the soil profile into the vadose zone below it (mm), and \(Q_{gw}\) is the return flow (mm). In SWAT+ the soil of an HRU also gains irrigation where the model applies it and loses lateral flow and tile flow; on an HRU with a wetland the precipitation and the irrigation go to the wetland first. The return flow \(Q_{gw}\) is computed by the aquifers, not by the HRU. The sum starts from \(SW_0\), the state the model is given for its first day. This is why a run needs a warm-up.

## Choose the period

The period of a run is its first year, its last year and its warm-up. SWATrust reads all three from the model and lets you change them for the run. The model of this page comes with 1997 to 2025 and a warm-up of 3 years, and holds weather for 1981 to 2025.

1. Click **Set-up** on the left of the page.
2. If the list **Models** holds other models, click **Clear choice** and tick **02070002 North Branch Potomac (unrouted)**, so that the line beside the heading ends "1 chosen".
3. In **First year**, type `2000` and press ++enter++.
4. In **Last year**, type `2015` and press ++enter++.
5. In **Warm-up**, leave `3`, or type it and press ++enter++ if you changed it before.

    The line under the boxes reads "16 years, the first 3 as warm-up. Weather: 1981 to 2025." The run simulates 2000 to 2015 and writes 2003 to 2015 to the tables.

--8<-- "include/shots/s06_1_period.html"

SWATrust writes the period into the files of its copy of the model, where SWAT+ reads them: the years into `time.sim` and the warm-up into `print.prt`. In the copy of this run the lines read as follows.

```text
time.sim
 DAY_START YRC_START DAY_END YRC_END  STEP
         0      2000       0    2015     0

print.prt
 N_Yrs_SKIP   JD_START  YRC_START     JD_END    YRC_END   INTERVAL
          3          0          0          0          0          1
```

### Years the page refuses

A period that the model cannot run is refused in Set-up, before any run, with the years that can be typed. Three cases, each with the sentence the page gave:

- First year `1970`, last year `2015`: "The first year, 1970, is before the model's weather, which starts in 1981. Choose a first year from 1981 to 2015."
- First year `2010`, last year `2005`: "The last year, 2005, is before the first year, 2010. Choose a last year from 2010 to 2025."
- First year `2010`, last year `2013`, warm-up `4`: "The warm-up, 4 years, leaves no year to print: the run simulates 4 years. Choose a warm-up from 0 to 3."

While a period is refused, **Start the run** is off, and the **Run** view repeats the sentence under **Checks before the run**.

--8<-- "include/shots/s06_2_refused.html"

### Why the warm-up matters

The warm-up years are simulated, but not written to the tables. They let the soil water, the snow, the groundwater and the plant cover move away from the values the model starts with. The plant cover is the slowest of these. Where plants start from nothing, as on the urban land of this model, they take many years to grow, and their cover sets how much water evaporates from the soil. The two runs of this tutorial show the effect on the same year, 2011, in mm over the basin:

| Run | Years simulated before 2011 | Precipitation | Evapotranspiration | Water yield |
|---|---|---|---|---|
| 2010 to 2013, warm-up 1 ([Quick start](quick-start.md)) | 1 | 1,311.8 | 647.7 | 221.7 |
| 2000 to 2015, warm-up 3 (this page) | 11 | 1,311.8 | 616.1 | 231.0 |

The precipitation of 2011 is the same in both runs, because it is an input. Evapotranspiration and water yield differ, because the two runs reach 2011 from different states.

Runs that start in different years can give different daily flows on days of high flow, even years after the start, because the same water can leave a channel a day earlier or later. Once both runs have had a few years of warm-up, their monthly and yearly flows agree closely, so compare such runs by month or year.

## Check the output tables

The column **Output tables** shows which tables the run writes and at which time steps. A tick under **Day**, **Mon** or **Year** gives one line for each day, month or year; a tick under **Avg** gives the average of the printed years.

1. Under **Entire basin**, see that **Water balance** carries its four ticks.

    They give the water balance of the basin by day, by month, by year and as the average year. The model asks for the last three. SWATrust adds the tick under **Day**, because the **Results** view draws from that table, and says so under the list: "SWATrust ticked 1 table for the Results view."

2. Leave the other ticks unchanged, and click **Continue to Run**.

--8<-- "include/shots/s06_3_tables.html"

The daily flow at the outlets needs no tick. The model asks for these records itself, in its file `object.prt`, and the run writes one file for each of them.

!!! note "Calibrated values"
    Under **Paths and period**, the line **Calibrated values** reads "the model's own": the run applies the file `calibration.cal` that came with the model and that its `file.cio` names. Keep it for this run. [Calibrate and validate](calibrate.md) makes a new file.

!!! note "Tables and disk space"
    Each tick adds to the size of the output. The **Run** view gives the room that the run needs before the start, and the **i** beside that line divides it into the copy of the model and the output tables.

## Run

The **Run** view shows the run before it starts: under **Checks before the run** the two checks, and in the table the basin with its years, 2000 to 2015, and its warm-up, 3.

1. Click **Start the run**.

    The line of the basin reads **Running** and says what the engine has done so far. In a run on this launcher it read first "reading the model's files", then "output tables opened (…), no year written yet", where the bracket gives the number and the size of the files, and later "simulated to April 2000". The **i** beside the heading of the table says that the progress is an estimate, so the year moves in steps and may first show late.

    --8<-- "include/shots/s06_4_running.html"

2. Wait until the page reads "1 of 1 basin finished."

    The table gives the state, the run time, the peak memory and the size of the output tables. **Run details**, under the table, gives the years, the warm-up and the size of the model copy. The run time and the memory are those of your computer for this run.

3. Click **See the results**.

--8<-- "include/shots/s06_5_finished.html"

The run folder keeps one line for each basin of the run in the file `basins.csv`: the state, the years, the warm-up, the threads asked and the threads used, the run time, the peak memory and the sizes.

## Read the flow at the outlet

The **Results** view opens on the basin you just ran. The box **Basin** at the top of the left column lists the basins that have results.

In the middle column, the chart under the basin draws the simulated flow at the basin outlet in m³/s from 2003, the first year after the warm-up. The line over the chart reads "Flow at the outlet".

To look at a part of the period, click **Zoom** and draw a box on the chart. **Zoom out** shows the whole period again.

Under the chart, a small table gives five figures of the flow. In the run of this page it read as follows.

| | Mean | Highest | Low flow | High flow | mm yr⁻¹ |
|---|---|---|---|---|---|
| This run | 49.3 | 460 | 16.3 | 162 | 444 |

The first four are in m³/s. The low flow is passed on 95 days in 100 and the high flow on 5 days in 100, over the years written to the tables. The last column is the mean flow as a depth over the land that drains to the point, in mm a year.

--8<-- "include/fig/fig06_flow.html"

### The file behind the chart

The chart is drawn from one file of the run, `020700020803_con.out`, in the output folder of the basin. In **Results**, the row of the basin under **Output folders** has the button **Open output folder**. The file is at this place:

```text
~/SWATrust/runs/run_<date>_<time>/02070002/out/020700020803_con.out
```

The first line of the file names its columns, and each line after it is one day, from the first simulated day. The warm-up years are in the file, so it starts on 1 January 2000. The columns that matter for flow:

| Column | Holds | Unit |
|---|---|---|
| `jday` | day of the year | |
| `mon`, `day`, `yr` | month, day of the month, year | |
| `name`, `type` | the kind of point (`outlet`) and the name of the record (`out_020700020803`) | |
| `flo` | volume of water that passed on that day | m³ |
| `sed` | sediment | metric tons |
| `orgn`, `no3` | organic nitrogen, nitrate | kg N |
| `sedp`, `solp` | organic phosphorus, soluble phosphorus | kg P |

The engine writes a volume for each day. The page derives the flow in m³/s of its chart from it, as that volume divided by the seconds of a day:

\[
Q = \frac{V_{day}}{86{,}400}
\]

where \(Q\) is the mean flow of the day (m³/s) and \(V_{day}\) is the value of the column `flo` (m³).

The file is a text table with its columns divided by spaces. The following Python script reads it without any added package and prints the number of days, the mean flow and the highest daily flow after the warm-up.

```python title="outlet_flow.py"
# Daily flow at the basin outlet, read from the outlet's daily record of a run.
# Usage: python3 outlet_flow.py <file> <first year>
import sys

path = sys.argv[1]
first_year = int(sys.argv[2])
flows = []
with open(path) as f:
    names = f.readline().split()
    i_yr, i_flo = names.index("yr"), names.index("flo")
    for line in f:
        parts = line.split()
        if int(parts[i_yr]) >= first_year:
            flows.append(float(parts[i_flo]) / 86400.0)  # m3 per day to m3/s
print(len(flows), "days")
print("mean flow %.1f m3/s" % (sum(flows) / len(flows)))
print("highest daily flow %.1f m3/s" % max(flows))
```

1. Save the script as `outlet_flow.py`.
2. Run it on the file of your run, with the first year after the warm-up.

    ```bash
    python3 outlet_flow.py ~/SWATrust/runs/run_<date>_<time>/02070002/out/020700020803_con.out 2003
    ```

    For the run of this page it printed:

    ```text
    4748 days
    mean flow 49.3 m3/s
    highest daily flow 460.5 m3/s
    ```

The run writes one such file for each of the 37 outlets that the model's `object.prt` lists. That file also gives each record its file name, a 12-digit number followed by `_con.out`. All 37 files have the same columns.

## Read the water balance

On the left, **Water balance, average year** shows the parts of the water balance of the land for the average of the years written to the tables, 2003 to 2015. Each part is given in mm over the land area of the basin and as a share of the precipitation. The last row, **Outlet flow**, is the mean flow at the basin outlet as a depth over the same land. In the run of this page the table read as follows.

| Part | mm | % of precip. |
|---|---|---|
| Precipitation | 1,043 | 100 |
| ET | 613 | 59 |
| Surface runoff | 111 | 11 |
| Lateral flow | 45.4 | 4 |
| Baseflow | 140 | 13 |
| Deep seepage | 26.6 | 3 |
| Channel loss | 1.3 | 0 |
| Outlet flow | 444 | 43 |

--8<-- "include/shots/s06_7_wb_avg.html"

The **i** beside the heading says that not every part is listed, so the parts need not add up.

**Output checks**, above it, gives a few of the same values as shares: evapotranspiration and surface runoff as shares of the precipitation, and baseflow as a share of the water that the land and the aquifers give the channels.

The values of each year are in the file `basin_wb_yr.txt` of the run folder. Its first three lines for this run, rounded to 0.1 mm:

<div class="wide" markdown>

| `yr` | `precip` | `et` | `wateryld` | `perc` | `surq_gen` | `latq` | `snomlt` | `sw_ave` |
|---|---|---|---|---|---|---|---|---|
| 2003 | 1,400.6 | 667.4 | 285.3 | 445.6 | 213.8 | 71.4 | 205.9 | 172.9 |
| 2004 | 1,145.9 | 650.6 | 172.3 | 348.4 | 115.7 | 56.6 | 142.8 | 153.7 |
| 2005 | 911.3 | 534.6 | 133.3 | 245.9 | 92.3 | 40.9 | 122.5 | 126.0 |

</div>

[Read the results](read-results.md) shows how to read this file with a few lines of Python.

Water yield is the water that leaves the land for the channels as surface runoff, lateral flow and tile flow:

\[
WYLD = Q_{surf} + Q_{lat} + Q_{tile}
\]

where \(WYLD\) is the water yield (mm), \(Q_{surf}\) is the surface runoff (mm), \(Q_{lat}\) is the lateral flow (mm) and \(Q_{tile}\) is the tile flow (mm). In 2003 the surface runoff, 213.8 mm, the lateral flow, 71.4 mm, and the tile flow, 0.1 mm, add up to the water yield of 285.3 mm.

The water balance of the entire basin is in four files of the run folder, one for each time step: `basin_wb_day.txt`, `basin_wb_mon.txt`, `basin_wb_yr.txt` and `basin_wb_aa.txt` (the average year). In each, the first line is a title, the second names the columns, the third gives their units, and the lines after it hold the values. The columns of this page:

| Column | Holds | Unit |
|---|---|---|
| `precip` | precipitation, rain and snow | mm |
| `snomlt` | snowmelt | mm |
| `surq_gen` | surface runoff generated on the land | mm |
| `latq` | lateral flow in the soil | mm |
| `wateryld` | water yield | mm |
| `perc` | water that percolates out of the soil profile | mm |
| `et` | evapotranspiration | mm |
| `qtile` | tile flow | mm |
| `sw_ave` | average soil water of the soil profile | mm |

### Why the outlet carries more than the water yield

The water yield is what the land sends to the channels, as a depth over the land area of the model, which is the area of its HRUs: 3,503 km². The page gives it in two rows, **Surface runoff** and **Lateral flow**, which add up to about 156 mm a year in this run. Over the same area, the row **Outlet flow** gives 444 mm a year.

On the way to the outlet the channels also receive the flow of the aquifers, about 140 mm a year in the row **Baseflow**, and the water of the 37 point sources of the model, about 147 mm a year. Neither is in the water yield. The three together make up nearly all of the outlet's flow.

The depth of the point sources is not on the page. It was computed from the point-source files of the model.

## What SWATrust does not do here

- The chart shows simulated flow only. Measured flow is not drawn beside it; the comparison with measured flow is part of [Calibrate and validate](calibrate.md).
- The Results view draws the flow at the basin outlet and from each subbasin. The flow in 24 channels is in the files of the run.

## References

Neitsch, S.L., Arnold, J.G., Kiniry, J.R., Williams, J.R., 2011. Soil and Water Assessment Tool theoretical documentation, version 2009. Texas Water Resources Institute Technical Report No. 406. Texas A&M University System, College Station, Texas.

## Video

--8<-- "include/slots/06_run_streamflow.html"

## Next

[Find the outputs](outputs.md) goes through the folder of a run and the names of its tables.

<p class="checked">Checked on SWATrust launcher 1.0.0 on Linux x86-64, on 20 November 2026.</p>
