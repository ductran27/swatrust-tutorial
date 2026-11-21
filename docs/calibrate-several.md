# Calibrate on several gauges and variables

This page shows how to calibrate a model on more than one measured series: the flow at several gauges, and variables other than flow.

## What you need

- The steps of [Calibrate and validate](calibrate.md), which this page builds on.
- A model in **Set-up**. This page uses the basin 02070002, for which the Calibration page lists two gauges of the U.S. Geological Survey (USGS).
- A measured file for each series that the page does not download.

## One row for each measured series

Under **Measured data**, the Calibration page has one row for each measured series. The page says of the rows: "One row is one measured series: a variable, where it is measured, and its file. Choose takes your own file, and the unit is chosen beside it. A calibration scores each row on its own days and takes the mean over the rows. At most 8 rows."

The first row is the flow at the gauge of the model. Its **Variable** reads "Streamflow", and its **Where** names the channel of the model at the gauge, "Channel 1496 (at the gauge)" for the basin 02070002. The menu **Where** marks three of its entries: "Outlet 10 (USGS 01598500)", "Outlet 37 (basin outlet)" and "Channel 1496 (at the gauge)".

To add a row:

1. Click **Add measured data**. A second row stands under the first, with the menus **Variable** and **Where**, the box **Measured file** with the button **Choose**, the menu **Unit** and the button **Remove**.
2. In **Variable**, choose what the file measures.
3. In **Where**, choose the channel of the model at the place of the measurement.
4. Under **Measured file**, give the file.

To take a row out again, click its **Remove**.

## The gauges of the model

The band **USGS gauges** lists the gauges that the page knows for the model.

1. Under **Measured file** of the first row, click **USGS gauges**. The band comes into view.
2. In the band, click the number of a gauge. The band names the gauge and its record.

For the basin 02070002 the band lists two gauges.

| Gauge | The band reads |
|---|---|
| USGS 01603000 | "USGS 01603000, North Branch Potomac River near Cumberland, Maryland" and "Daily flow since 1929-05-24. Basin 02070002 North Branch Potomac." |
| USGS 01598500 | "USGS 01598500, North Branch Potomac River at Luke, Maryland" and "Daily flow since 1899-06-27. Basin 02070002 North Branch Potomac." |

The first row of **Measured data** uses the gauge 01603000: under **Measured file** it reads "This HUC uses USGS 01603000, North Branch Potomac River near Cumberland, Maryland".

### Download the flow of a second gauge

To calibrate on the second gauge as well, give that gauge a row of its own.

1. In the first row, click **Download**. While the page waits for the answer, it reads "asking USGS…". The box under **Measured file** then holds the file of the first gauge.
2. Click **Add measured data**. Leave **Variable** of the new row at "Streamflow".
3. In **Where** of the new row, choose "Outlet 10 (USGS 01598500)", the entry that carries the number of the second gauge. The row then names the gauge, "USGS 01598500, North Branch Potomac River at Luke, Maryland", and has a button **Download**.
4. In the new row, click **Download**. The box of the row then holds the file of the second gauge.

With the two files, each row reads "Read as daily values: 10,592 days, 1997-01-01 to 2025-12-31, m³/s". Under the new row the page adds: "A calibration with this file scores calibration 2000 to 2012 and validation 2013 to 2025."

Each download asks USGS and so needs the internet. The page writes both files into the folder `obs` of the model.

## Variables other than flow

The menu **Variable** of an added row has six entries. The row changes with the variable: the menu **Unit** lists the units of the variable, and the empty box under **Measured file** names the form of a line of the file.

| Variable | Units in **Unit** | The empty box reads |
|---|---|---|
| Streamflow | m³/s first | Date, flow in m³/s |
| Suspended sediment | mg/L, t/day, short tons/day | Date, value |
| Nitrate | mg/L as N, kg/day as N, lb/day as N | Date, value |
| Total nitrogen | mg/L as N, kg/day as N, lb/day as N | Date, value |
| Total phosphorus | mg/L as P, kg/day as P, lb/day as P | Date, value |
| Evapotranspiration | mm/month, in/month | Month, value |

The page says of a file of sediment or of a nutrient: "One text file, one measurement on a line: the date and the value, as in 2019-03-14, 2.1. Dates as 2019-03-14 or 3/14/2019. A date may repeat: the mean of the day's samples is scored. A value that starts with < is a sample below the reporting level, given as the level. A line that starts with # is a note."

For sediment the page adds beside **Variable**: "The model's sediment is all the channel sends out; USGS measures suspended sediment."

Evapotranspiration is compared for the whole basin, so its row has no menu of channels: **Where** reads "Whole basin". The page says of this row: "The model's evapotranspiration of the whole basin is compared month by month. Monthly evapotranspiration from satellite data is an estimate made by other models, not a measurement." Its file has one month on a line: "the month and the value, as in 2019-03, 61.5".

## What the page refuses

Before a start, the page names what a row still lacks. In a set-up for SUFI-2 of the basin 07080207 with a second row of Suspended sediment, the page writes these lines under **Checks**, after the name of the model:

| The second row | The page reads |
|---|---|
| has no entry under **Where** | "a row after the first names no channel." |
| has its channel and no file | "In the row Suspended sediment, Channel 401: Give the measured file's full path." |

A **Download** of suspended sediment needs a unit that USGS gives. With **Unit** at "t/day", a press gives no file, and the page reads under the row: "USGS gives suspended sediment in mg/L, as a concentration, or in short tons/day, as a load. Set this row's unit to one of the two, then press Download."

## How several rows are scored

A calibration scores each row on its own days and takes the mean over the rows, as the page says beside **Measured data**. With more than one row, the menu of the statistic in the set-up of GLUE and of SUFI-2 reads "NSE" and "KGE"; with one row it reads "NSE daily" and "KGE daily".

After an analysis with SUFI-2 on two rows, the table of the tab **Simulations** has a column "Mean KGE", with "over the rows" under its name, beside the statistics of the row in view.

## Read the result

The result of an analysis with more than one row shows one row at a time. After an analysis with SUFI-2 on two rows of the basin 07080207, a menu of the result names the rows, "Streamflow, Outlet 40" and "Suspended sediment, Channel 401", and the chart and the tables follow the row chosen in it.

| Row chosen | The chart is headed | The table of the band counts |
|---|---|---|
| Streamflow, Outlet 40 | "Daily flow" | "Measured days" |
| Suspended sediment, Channel 401 | "Suspended sediment" | "Sampled days", "Samples" and "Below the reporting level" |

For the row of samples, the statistics of the best simulation are those of the "sampled days".

## Next

- [Uncertainty analysis](uncertainty.md) puts a band around the simulated flow.
