# Read the results

This page shows how to read the Results view of a run and the tables that the run wrote.

The run of this page is the run of [Run streamflow](run-streamflow.md): the basin 02070002, 2000 to 2015, with a warm-up of three years.

## The three columns of Results

Click **Results** in the left column of the page. The view has three columns.

- The left column sums the run up: **Output checks**, **Water balance, average year** and **Output folders**.
- The middle column shows the basin as a block on its relief, and the daily flow under it.
- The right column gives the counts of the basin or of one subbasin, the values of the day shown, and a table of the subbasins.

The box **Basin** at the top of the left column chooses what the view shows. It lists the basins that have results. The heading of the view gives the years that the run wrote to its tables, here 2003–2015.

--8<-- "include/shots/s08_1_results.html"

## The checks of the output

**Output checks** is a short table of checks on the output of the run. Point at a row to read what it means. In a window that is not high enough for the six rows, the table shows the first of them, and the others stand below them in the same box.

The page says of the rows:

- **ET share**: "ET as a share of precipitation, average year. Irrigation is not counted in precipitation, so the share can pass 100 %."
- **Baseflow share**: "Baseflow as a share of the water that the land and the aquifers give the channels, average year."
- **Surface runoff**: "Surface runoff that reaches the channels, as a share of precipitation, average year. Where the model irrigates, part of it is irrigation water."
- **Missing days**: "Days of the printed years with a missing or negative flow at the outlet", with the number of days of those years.
- **Calibrated values**, for this run: "The run applied the model's own file of calibrated values, the one its file.cio names."
- **Daily flow table**: "The run wrote the daily flow of the model's outlets."

--8<-- "include/shots/s08_2_checks.html"

## The water balance of the average year

**Water balance, average year** gives parts of the water balance of the land in mm and as a share of the precipitation. The line above the table gives the land area that the depths refer to. [Run streamflow](run-streamflow.md#read-the-water-balance) reads the table for this run.

The page says of each part:

- **Precipitation**: "Rain and snow on the land."
- **ET**: "Evapotranspiration."
- **Surface runoff**: "Runoff over the ground that reaches the channels."
- **Lateral flow**: "Flow through the soil that reaches the channels."
- **Baseflow**: "Flow of the aquifers to the channels."
- **Deep seepage**: "Water that leaves the aquifers downward."
- **Channel loss**: "Evaporation and seepage of the channels."
- **Outlet flow**: "The mean flow at the basin outlet over the printed years, as a depth over the same land area."

The **i** of the table says: "Each part for the average year, in mm over the land of the basin. Not every part is listed, so they need not add up."

## The map and the day

The middle column draws the basin as a block on its relief, with its streams as blue lines and its outlet as a red dot. The color of each subbasin is its value on the day shown, and the date of that day stands beside **Play**. Drag the block to turn it, use the wheel to zoom, and double-click to set it back. Two bands on the sides of the block show soil water (upper) and groundwater (lower), in mm, for each subbasin on the basin's edge on the day shown. A band is darker and taller where the value is higher.

1. Choose a value in the list **Color by**: Flow, Runoff, ET, Soil water, Snow or Groundwater. The scale beside the list gives the lowest and the highest value of the colors.
2. Click **Play**. The date moves through the run, and the subbasins change color. Click **Pause** to stop.
3. Click a place in the chart of flow to go to that day.

The right column gives the same six values for the day shown, under **On** and the date. The flow is a value of each day. The other values have the step of the tables that the run wrote: with the tables of this run, the page marks runoff, ET, soil water and snow "mm, month" and groundwater "mm, year". Point at one of these rows, and the page names the box of **Output tables** to tick for a value of each day.

A tick in front of a value adds it as a column to the table of subbasins, at the foot of the right column. Up to three values can be ticked at once.

--8<-- "include/shots/s08_4_table.html"

## Flow at the outlet and from a subbasin

Under the block, the chart draws the daily flow at the basin outlet in m³/s, and the line above it reads "Flow at the outlet".

1. Click a subbasin on the block, or a row of the table of subbasins. The line above the chart now reads "Flow from" with the code of the subbasin, and the chart draws the flow from that subbasin. The right column gives the subbasin's area, the area that drains to it, its elevation, and its numbers of HRUs, channels and reservoirs.
2. Click **Entire basin** to go back.

--8<-- "include/shots/s08_3_subbasin.html"

To look at a part of the period, click **Zoom** and draw a box on the chart: press the mouse button at one corner of the part you want and let it go at the opposite corner. The chart then shows the days and the flows inside the box. **Zoom out** shows the whole period again.

--8<-- "include/shots/s08_5_zoom.html"

The table under the chart gives the mean flow, the highest flow, the low flow and the high flow of the point shown, and the mean flow as a depth over the land that drains to it. The page says of it: "Low flow is passed on 95 days in 100, high flow on 5 days in 100, over the printed years." [Run streamflow](run-streamflow.md#read-the-flow-at-the-outlet) explains the five values.

The table of subbasins in the right column lists every subbasin with its area, the area that drains to it, and its flow on the day shown.

## The files of the run

**Output folders** lists each basin that has results, with a button **Open output folder**. [Find the outputs](outputs.md) describes the files.

The values of each month and each year are not on the page. The rest of this page reads them from the files.

## Read a table with your own program

The Results view draws the flow and the water balance. For every other question you read the tables themselves. They are plain text, so a spreadsheet, R or Python reads them.

A table has three head lines: a title, the names of the columns and their units. Each line after them is one object and one step. The words of a line are divided by spaces.

```text
 jday   mon   day    yr    unit  gis_id  name                  precip     snofall      snomlt    surq_gen        latq    wateryld
                                                                  mm            mm          mm          mm          mm          mm
  365    12    31  2003       1       1  <model>             1400.591     199.562     205.943     213.782      71.443     285.319
  366    12    31  2004       1       1  <model>             1145.854     145.756     142.783     115.708      56.590     172.329
```

The listing leaves out the title line, which is the first line of each table. In the column `name` it writes `<model>` where the file holds the name of the model, as the files of the model give it.

The following lines of Python read such a table. They need no package.

```python
def read_table(path, head_lines=3):
    """Read a SWAT+ output table. Return one dictionary for each line."""
    with open(path) as f:
        lines = f.read().splitlines()
    names = lines[head_lines - 2].split() if head_lines == 3 else lines[0].split()
    rows = []
    for line in lines[head_lines:]:
        rows.append(dict(zip(names, line.split())))
    return rows

def read_record(path):
    """Read the daily record of one object (a file named in object.prt)."""
    return read_table(path, head_lines=1)
```

`read_table` pairs the words of each line with the column names, in their order. Every value is text: turn it into a number with `float` where you reckon with it.

To print the precipitation, the water yield and the evapotranspiration of each year:

```python
for row in read_table("basin_wb_yr.txt"):
    print(row["yr"], row["precip"], row["wateryld"], row["et"])
```

```text
2003 1400.591 285.319 667.449
2004 1145.854 172.329 650.648
2005 911.296 133.262 534.569
```

Three things to know before you read other tables.

- **A line can be shorter than the names line.** The tables of the entire basin leave out the last columns that hold words, `plant_cov` and `mgt_ops`. The pairing in order is still right for every column that has a value.
- **Do not count the words of the units line.** A column without a unit has a blank there, so the units line has fewer words than the names line. Read a unit from the place under the column's name.
- **The average-year table ends with extra words.** The line of `basin_wb_aa.txt` ends with words that belong to no column. The pairing in order is right for the columns before them.

## Read the record of an outlet

A record has one head line and no units line, and it holds every simulated day, the warm-up years too. `read_record` reads it.

To add up the volume of each year at the basin outlet and turn it into a mean flow:

```python
days = {}
volume = {}
for row in read_record("020700020803_con.out"):
    year = row["yr"]
    days[year] = days.get(year, 0) + 1
    volume[year] = volume.get(year, 0.0) + float(row["flo"])
for year in sorted(volume):
    print(year, round(volume[year] / 86400 / days[year], 1))
```

```text
2003 76.6
2004 59.5
2005 48.4
```

`flo` is the volume of water of a day in m³. A day has 86,400 seconds, so the volume of a year divided by 86,400 and by the number of its days is the mean flow of that year in m³/s. The lines print the warm-up years, 2000 to 2002, as well; they are left out here, and [Run streamflow](run-streamflow.md) says why they are not used.

## Video

--8<-- "include/slots/08_read_results.html"

## Next

- [Run sediment](run-sediment.md) reads the sediment that leaves the land and the channels.
- [File reference](files.md) lists the head lines and the columns.
