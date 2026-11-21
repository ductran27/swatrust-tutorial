# Quick start

This page takes you from the SWATrust folder to the daily flow of a first basin in a few steps.

You run one basin, 02070002 (North Branch Potomac), for four years and look at the flow at its outlet. Nothing is installed, and the folder of the model is not changed.
!!! note "Before you start"
    You need the SWATrust folder for your computer, unpacked, and a web browser. The first step of the page downloads the basin, so the computer also needs a connection to the internet.[Download](download.md) says where the folder comes from, and [Install and start SWATrust](install.md) how to start it. The steps of this page were done on Linux.

## The basin of this chapter

The basin is the SWAT+ model of the North Branch Potomac River, hydrologic unit 02070002, one of the HUC8 models that the page downloads. [Get a model](models.md) describes them. The page shows these counts once the model is read.
| Part of the model | Count |
|---|---|
| Area | 3,531 km² |
| Hydrologic response units (HRUs) | 895 |
| Routing units | 74 |
| Channels | 1,658 |
| Aquifers | 37 |
| Reservoirs | 85 |
| Point sources | 37 |
| Outlets | 37 |
| Period of the model | 1997 to 2025 |
| Weather in the model | 1981 to 2025 |

## Start SWATrust

SWATrust runs in a terminal window and shows its page in your browser. Start it from its own folder, where its engine and the basin are.

1. Open a terminal and go to the SWATrust folder.

    ```bash
    cd ~/SWATrust-linux-x86_64
    ```

2. Start the launcher.

    ```bash
    ./swatrust
    ```

    SWATrust prints the folder of its runs and the address of its page.

    ```text
    SWATrust launcher 1.0.0
      engine:  /home/user/SWATrust-linux-x86_64/swatrs (Linux x86-64)
      runs in: /home/user/SWATrust/runs
      lists:   models.json and history.json in the runs folder
      maps:    /home/user/SWATrust-linux-x86_64/swatrust_maps.pack (… basins)
      open:    http://127.0.0.1:52811/?t=4f0c...
    Keep this window open while you use the launcher. Ctrl-C stops it and any run it started.
    ```

3. Open the address after `open:` in your browser if the page has not opened by itself.

!!! note "The address holds a key"
    The part after `?t=` is a key, and SWATrust makes a new one at each start. A page opened without the key shows only a short text that asks for the address the launcher printed, so copy the whole address.

--8<-- "include/shots/s02_1_first.html"

## Put the basin in the list

The page opens on **Set-up**, the first of the four views named in its left column. At the first start the list **Models** is empty: it reads "No model yet" and names two ways to get a model, **Add a model folder** for your own model and **Download** for a basin under the map. This page takes the second.

1. Under the map, type `02070002` in the box **Code or name**. The page marks the row of the basin.
2. Leave **Basin alone**, and click **Download**.

    While it works, the page reads "Checking 02070002 North Branch Potomac…" and "Downloading 02070002 North Branch Potomac" with how much has arrived. When the model is there, it reads "02070002 North Branch Potomac is in the list of models." [Get a model](models.md#download-a-basin-from-the-page) describes the list under the map and the two forms of a model.

    The basin appears in the list **Models** with its 895 HRUs and its years, 1997 to 2025, and the line above the list reads "1 found, 1 chosen". On the map under the list, the basin is drawn in yellow. To see the relief of the basin in colors, from 164 m to 1,236 m, with its streams and a red dot at its outlet, click **This basin** above the map.

--8<-- "include/shots/s02_2_ticked.html"

The middle column, **Paths and period**, now shows the model: its folder, the folder of the output, its file of calibrated values, the years of the run, and the counts of its parts under **The model**. The right column, **Output tables**, lists the tables that the run writes.

## Choose four years

The model comes with the period 1997 to 2025. A first look does not need 29 years, so you give the run a shorter period.

1. In **First year**, type `2010` and press ++enter++.
2. In **Last year**, type `2013` and press ++enter++.
3. In **Warm-up**, type `1` and press ++enter++.

    The line under the boxes now reads "4 years, the first as warm-up. Weather: 1981 to 2025." The warm-up year, 2010, is simulated, but not written to the tables, so the results start in 2011.

4. Leave **Output tables** as it is, and click **Continue to Run**.

--8<-- "include/shots/s02_3_years.html"

!!! note "A run writes nothing into the model folder"
    The years you type go into a copy of the model that SWATrust makes for the run.

## Run the basin

The **Run** view opens. On the left, **Threads** holds the box **Threads in this basin**; leave it as it is. Under **Checks before the run**, two lines in green say that the disk has room for the run and that the weather data of the model cover the years of the run. On the right, the table lists the basin with its years and its warm-up, and the word "ready".

--8<-- "include/shots/s02_4_run_ready.html"

1. Click **Start the run**.

    The line of the basin reads **Running**, with the number and the size of the output tables that the engine has opened and, later, the month and the year that the run has reached.

2. Wait until the page reads "1 of 1 basin finished."

    The table then gives the state **Finished**, the run time, the peak memory and the size of the output tables of this run on your computer. **Run details**, under the table, gives the years and the warm-up of the run.

3. Click **See the results**.

--8<-- "include/shots/s02_5_finished.html"

## Look at the results

The **Results** view shows the run in three columns.

- On the left, **Output checks** and **Water balance, average year** sum the run up, and **Output folders** has the button **Open output folder** for the basin of the run.
- In the middle, the basin is drawn as a block on its relief, with each subbasin in the color of its value on the day shown. Under it, a chart draws the daily flow at the basin outlet in m³/s, from 2011, the first year after the warm-up, to the end of 2013.
- On the right are the counts of the basin, its values on the day shown, and a table of the subbasins.

--8<-- "include/shots/s02_6_results.html"

1. Read the table **Water balance, average year**. It gives the parts of the water balance of the land in mm and as a share of the precipitation. In the run of this page it read as follows.

    | Part | mm | % of precip. |
    |---|---|---|
    | Precipitation | 1,082 | 100 |
    | ET | 651 | 60 |
    | Surface runoff | 101 | 9 |
    | Lateral flow | 47.4 | 4 |
    | Baseflow | 146 | 13 |
    | Deep seepage | 26.2 | 2 |
    | Channel loss | 1.4 | 0 |
    | Outlet flow | 441 | 41 |

2. Click **Play**. The date moves through the run, and the subbasins change color with the value chosen under **Color by**. Click **Pause** to stop.

3. Click a row of the table of subbasins, or a subbasin on the block. The chart now draws the flow from that subbasin, and the right column gives its counts. Click **Entire basin** to go back.

--8<-- "include/shots/s02_7_subbasin.html"

Under **Output folders**, the basin of the run has the button **Open output folder**. The files of the run are in the folder `out` of the basin, inside the folder of the run; [Find the outputs](outputs.md) describes them.

The values of each year are not on the page. They are in the file `basin_wb_yr.txt` of the run; [Read the results](read-results.md) shows how to read it.

## Stop SWATrust

The launcher runs until you stop it. The runs you made stay in the runs folder and are listed again at the next start.

1. Go to the terminal window and press ++ctrl+c++.

    SWATrust answers `swatrust: stopped.`

## What SWATrust does not do here

- Six output tables that this model asks for are not written by this version: the channel summary of the basin; the water balance, the nutrient balance, sediment and nutrients, and plants and weather by landscape unit; and the nutrient balance by HRU. Their boxes under **Output tables** cannot be ticked. The run leaves them out and writes every other table.
- The Results view shows the flow and the water balance. Sediment and nutrients are in the output tables; [Run sediment](run-sediment.md) and [Run water quality](run-water-quality.md) show how to read them.

## Video

--8<-- "include/slots/02_quick_start.html"

## Next

[Run streamflow](run-streamflow.md) runs the same basin over a longer period and reads the flow at the outlet from its file.

<p class="checked">Checked on SWATrust launcher 1.0.0 on Linux x86-64, on 20 November 2026.</p>
