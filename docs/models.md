# Get a model

This page shows how to get a SWAT+ model of a United States basin and add it to SWATrust.

## The basin of the quick start

[Quick start](quick-start.md) runs the basin 02070002 (North Branch Potomac), one of the HUC8 models below. It downloads the model from the page, in the way this page shows for another basin.

## The HUC8 models

The other models of this tutorial come from a published data set of SWAT+ input files for HUC8 basins of the conterminous United States (Tran, 2026). The [Glossary](glossary.md#the-parts-of-a-swat-model) explains a HUC8 basin. The data set has the license CC BY 4.0, and its address is https://doi.org/10.6084/m9.figshare.35018494. Each model is one folder. The name of the folder is the eight-digit code of the basin.

## Download a basin from the page

SWATrust can fetch one basin of the data set for you.

1. Open **Set-up** and look under the map.

    The page lists the basins of the data set there, each with its code, its name and the size of its download. The "i" beside the buttons **Basin alone** and **With inflow from upstream** says "A basin you download is added to the list of models." and names the source of the data, https://doi.org/10.6084/m9.figshare.35018494, and its license, CC BY 4.0.

2. Type the code of the basin, or a part of its name, in the box **Code or name** above the list. For this page, type `11140204`, the code of the basin Red Chute.

    The list then shows the basins that fit. When the whole eight-digit code is typed, the page marks the row of that basin. The box **All states** beside the first box shows the basins of one state. If no basin fits, the list reads "No basin has this code or name."

3. Choose the form of the model with the two buttons above the list. The page says of them: "Basin alone leaves out the inflow from upstream basins; With inflow from upstream brings in their daily outflow." For this page, leave **Basin alone**.

4. See that the row of the basin is marked. For a basin found by a part of its name, click its row.

    The line under the list gives the size of the download, the size on disk and the free space of your disk. The button **Download** is off until a basin is marked. After a click on a row, the box holds the code of that basin and the list shows all basins again. In the map of all basins, a click on a basin that is not among your models marks its row in the same way.

    --8<-- "include/shots/s04_4_get.html"

5. Click **Download**.

    While the download goes, the line under the list reads "Checking" and then "Downloading", each with the code and the name of the basin, and the button **Cancel** shows beside it. At the end the line reads "11140204 Red Chute is in the list of models." The model is then in the list **Models**, and it is chosen for the next run. SWATrust keeps a downloaded model in the folder `models` of its runs folder, under the code of the basin.

After the download, the row of the basin in the list ends "in the folder", and **Download** is off for it. With the row marked, the line under the list reads "Already in the models folder in this form."

## Add a model folder that you already have

1. In **Set-up**, click **Add a model folder**. A dialog lists the folders of your computer.
2. Go to the folder of the model. A click on the row of a folder opens it, and **Home** and **Launcher folder** go to those two folders. You can also type the path of the folder in the box at the top and press ++enter++.
3. Read the line at the foot of the dialog. For a model it says "This folder is a model (it holds file.cio)."
4. Click **Add this folder**.

--8<-- "include/shots/s04_1_add.html"

The model is now in the list **Models**, and it is chosen for the next run. Beside the button **Add a model folder** the page says "1 model added", and the line beside the heading says how many models were found and how many are chosen, for example "2 found, 1 chosen".

You can also add a folder that holds the folders of several models. The dialog then lists each of them with the word "model" and says how many it found, for example "4 model folders in this folder." Click **Add this folder**, and all of them are added. The page then says "4 models added".

## What Set-up shows for a model

Click the row of a model in the list **Models**, or choose it in the box **Model** of the middle column. The column **Paths and period** then shows that model. The click on the row does not change which models are chosen for the run; the tick at the left of the row does that.

| Line | What it shows |
|---|---|
| **Model folder** | the folder of the model |
| **Output folder** | a new folder in the runs folder for each run |
| **Calibrated values** | the file of calibrated values that the run uses |
| **First year**, **Last year**, **Warm-up** | the period of the run |
| **The model** | the elevation, the area and the counts of the parts |

A run works on a copy and changes no file of the model. The line **Calibrated values** reads "the model's own" or "the model has none", and **Choose** takes another file for the runs of this model. The line under the three boxes of the period says how many years run and for which years the model holds weather, for example "29 years, the first 3 as warm-up. Weather: 1981 to 2025." The block **The model** counts the aquifers, HRUs, reservoirs, routing units, point sources, channels and outlets.

--8<-- "include/shots/s04_2_facts.html"

The list **Models** gives the number of HRUs of each model and the first and last year of its period. Under the list is the map. It opens on **All basins**, which shows the basins of the data set in the conterminous United States, and the line above the map reads "Your models in yellow. Click a basin to choose it." **This basin** draws the model in relief, with its streams and a red dot at its outlet.

The USGS stations are on the Calibration page. Over the map of its band **USGS gauges**, under the label **USGS stations**, are four buttons: **Streamflow**, **Suspended sediment**, **Nitrogen** and **Phosphorus**. The page says of them: "A button of "USGS stations" shows the stations with data of that kind." [Calibrate and validate](calibrate.md) opens the band.

In the map of all basins, a click on a basin of yours ticks its model in the list **Models**, and a second click takes the tick out. A click on another basin marks its row in the list of basins under the map. **To chosen basins** draws the map around the chosen basins and writes the code and the name on each, and **Whole map** shows the whole map again.

--8<-- "include/shots/s04_3_all_basins.html"

## The flow from upstream

A basin that lies below another basin receives the flow of that basin. In a model, this flow enters at an inlet, and a point-source file of the model gives it for each day. **Set-up** says of these files: "Point sources are inflows from files, such as the outflow of a basin upstream."

### What Set-up shows for the inlet

For the basin 11140204, the block of the model shows two lines above **Model folder**.

| Line | What it says |
|---|---|
| "No inflow at 1 inlet" | an inlet without inflow data; its inflow is 0 |
| **Inflow from upstream** | "1 inlet", the size of the download and the button **Download** |

The "i" of the first line names the inlet: "Inlet 111402050307 has no inflow data, so its inflow is 0." The page says of the line **Inflow from upstream**: "The data set's daily outflow of the upstream basins at these inlets, as With inflow from upstream holds it, downloaded into this model's folder. No other file of the folder changes."

--8<-- "include/shots/s04_5_inlets.html"

1. In the line **Inflow from upstream**, click **Download**.

    SWATrust fetches the inflow file of the inlet into the folder of the model. The folder of 11140204 already holds this file, empty; the download fills it, and no other file of the folder changes. Under the list of basins the page then reads "1 inflow file of the data set is in the folder of 11140204." The line **Inflow from upstream** now gives the number of inlets and the last day of the file, "to 2025-12-31", and the line "No inflow at 1 inlet" is gone.

The inflow files of the data set hold every day from 1 January 1997 to 31 December 2025, with the exceptions that the README of the data set names. At an inlet, a run takes no inflow before the first day or after the last day of its file, unless the model upstream is in the list **Models**; SWATrust then runs that model first and takes its outflow.

### Which flow an inlet takes

In a run, each inlet takes the first source that it has. The file `README.txt` of the run names the sources in their order. In the two runs of 11140204 of the next section it read: "An inlet takes the first source it has: the flow of a USGS gauge (once downloaded), the model's inflow file, none." An inlet without a source has an inflow of 0 on each day.

### Read what each inlet took

SWATrust writes a file `README.txt` into the folder of a basin in the run folder when the model has inlets. The first line of the file names the basin, the time of the run, its years and its days. The file then has one line for each inlet, and the line names the source that the inlet took.

Before the download of the inflow file, the line of the run read:

```text
Inlet 111402050307: no inflow, 0 each day. No USGS gauge matches it, and its inflow file 111402050307_con.out holds no data.
```

After the download, the line of a new run read:

```text
Inlet 111402050307: the model's inflow file 111402050307_con.out (upstream model 11140205), 1997-01-01 to 2025-12-31.
```

### Upstream models in a run

SWATrust can also simulate the inflow of an inlet with the model of the basin upstream, when that model is in the list **Models**. For this page the model of 11140205 Bodcau Bayou, the basin upstream of 11140204, was added to the list and left without a tick. The inflow file of 11140204 had not been downloaded.

With 11140204 alone chosen, **Checks before the run** in the **Run** view had one more line: **Upstream models**, with the number 1.

After **Start the run**, the table of the run had two rows. The row of 11140205 came first, with the line "Upstream of 11140204 Red Chute (unrouted)" under its name. The row of 11140204 read "Waiting for the run of 11140205" until that run had ended.

In this run the `README.txt` of 11140204 named more sources: "An inlet takes the first source it has: the flow of a USGS gauge (once downloaded), its upstream model run with a calibration's values, the model's inflow file over the whole run, its upstream model run with its own parameters, the model's inflow file over part of the run, none." The line of the inlet read:

```text
Inlet 111402050307: the outlet of upstream model 11140205, run with its own parameters.
```

## A model that SWATrust does not run

This version of SWATrust does not include every part of SWAT+. A model that uses a part it does not include is not run, and the **Set-up** page says so. [Messages and troubleshooting](troubleshooting.md) lists the messages.
In the list under the map, such a basin carries the mark "not run". When its row is clicked, the line under the list gives the reason.

## References

Tran, D. (2026). SWATrust: SWAT+ input files for HUC8 basins of the conterminous United States [Dataset]. figshare. https://doi.org/10.6084/m9.figshare.35018494

## Video

--8<-- "include/slots/04_models.html"

## Next

- [Run your own model](own-model.md) adds a model that you built yourself.
- [Run streamflow](run-streamflow.md) runs the basin and reads the flow at its outlet.
