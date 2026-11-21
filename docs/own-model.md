# Run your own model

This page shows how to run a SWAT+ model that you built yourself, and what SWATrust does with its folder.

This page uses a copy of the basin 02070002 (North Branch Potomac). The copy lies in the folder `~/SWATrust/models/my_basin`, and its file `time.sim` runs from 2005 to 2014. It stands in for your own model.
## What counts as a model folder

A model folder is a folder that holds the file `file.cio` and the input files that it names. It is often named `TxtInOut`.

## Add the folder

1. In **Set-up**, click **Clear choice**. No model of the list is chosen now.
2. Click **Add a model folder**.
3. Go to the folder of your model, here `~/SWATrust/models/my_basin`. For a model, the dialog says "This folder is a model (it holds file.cio)."
4. Click **Add this folder**.

[Get a model](models.md#add-a-model-folder-that-you-already-have) shows the dialog.

The model is now in the list **Models** under the name of its folder, with its number of HRUs and the years of its file `time.sim`, 2005–2014. It is the only model chosen, and the line beside the heading ends "1 chosen".

The three boxes of the period hold the years of your model: 2005, 2014 and its warm-up of 3 years. The line under them reads "10 years, the first 3 as warm-up. Weather: 1981 to 2025."

--8<-- "include/shots/s05_2_years.html"

A model keeps its own years, warm-up and output tables, whatever other models are in the list. With several models in the list, the line beside the heading **Paths and period** counts them and adds "each with its own". The box **Model** under the heading then holds the model whose folders and years the page shows. To see or change the years of your model, pick it there. [Run several basins](run-many.md) describes a run of several basins.

The map under the list knows basins by their eight-digit code. For a folder with another name, the line above the map reads "my_basin: no map (the map knows basins by their 8-digit code)." when **This basin** is on.

For a folder that holds no model, the dialog says "No model in this folder or in the two levels below it: a model folder holds file.cio." **Add this folder** then adds nothing, and the page repeats the sentence under the button **Add a model folder**.

--8<-- "include/shots/s05_1_not_a_model.html"

## Run the model

1. Click **Continue to Run**. The table of the run lists the model under the name of its folder, with its years, 2005–2014, and its warm-up, 3.
2. Click **Start the run**, and wait until the line above the table reads "1 of 1 basin finished."
3. Click **See the results**. Beside the heading **Results**, the page gives the years that the run wrote to its tables, 2008–2014: the first three years are the warm-up, simulated, but not written to the tables.

[Run streamflow](run-streamflow.md) describes the **Run** view and the **Results** view.

## What SWATrust copies and what it leaves alone

A run does not write to the folder of your model. The page says of the folder: "A run works on a copy and changes no file of the model." Each run gets a new folder in the runs folder, with a copy of the model and the tables that the run writes. [Find the outputs](outputs.md) describes the folder of a run. The **Calibration** page adds one folder to the folder of the model: it keeps the measured flow there in a folder `obs`, as [Calibrate and validate](calibrate.md#get-the-measured-flow) shows.

## Models that this version does not run

This version of SWATrust does not include every part of SWAT+. A model that uses a part it does not include is not run, and the **Set-up** page says so. [Messages and troubleshooting](troubleshooting.md) lists the messages.

## Video

--8<-- "include/slots/05_own_model.html"

## Next

- [Run streamflow](run-streamflow.md) runs a basin and reads the flow at its outlet.
- [Find the outputs](outputs.md) shows the folder of a run.
