# Run several basins

This page shows how to run several basins in one go and read the table of the run.

## The basins of this page

This page runs five basins together: the basin 02070002 (North Branch Potomac) and four small HUC8 models. The [Glossary](glossary.md#the-parts-of-a-swat-model) explains a HUC8 model.
| Basin | Name |
|---|---|
| 02070002 | North Branch Potomac |
| 12110207 | Central Laguna Madre |
| 18070201 | Seal Beach |
| 04150600 | Chaudiere River |
| 03050210 | St. Helena Island |

[Get a model](models.md) shows how to get them and add them.

## Choose the basins

1. In **Set-up**, click **Clear choice**.
2. Tick each model that you want to run. The line beside the heading of the list says how many models are found and how many are chosen.
3. Click **Continue to Run**.

With several models chosen, the **Run** page runs them together, and the line beside its heading says how many basins are chosen in **Set-up**. To run one basin alone, choose only that basin in **Set-up**.

## The years of each basin

Each basin runs with the years, warm-up and tables set for it in Set-up. The table lists each basin with its years, its warm-up and the word "ready".

## Read the checks before the run

**Checks before the run** has one line for each thing that SWATrust checked. With the basins of this page it read as follows.

| Line | What it says |
|---|---|
| the disk | "Disk space: about … needed, … free" |
| the weather | "Each model's weather data cover the years of its run" |

A basin that takes water from a basin upstream can bring one more line, **Upstream models**. [Get a model](models.md#upstream-models-in-a-run) shows it.

## Basins at once and threads in each basin

The block **Threads** has two boxes. **Basins at once** sets how many basins run at the same time. **Threads in each basin** sets the number of threads that the engine uses inside each basin. The [Glossary](glossary.md) explains a thread. The number of threads is a setting of the run. It changes no input file.

Both boxes may stay empty. The page says of the first: "Left empty, SWATrust chooses from this machine's threads and memory." With the second box empty, each basin runs on one thread.

## Start and watch

1. Click **Start the run**.

    The page reads "The run is going. Its settings stay until it ends or is stopped.", and the button **Stop all** stands where the start button stood.

2. Watch the lines under **Basin, progress and threads**.

    Each basin has a line with its state. A basin that runs reads "Running" and says what the engine has done so far: first "reading the model's files", then the number of output tables that it has opened, and later the month that the run has reached, for example "simulated to July 2000". A basin that waits for its turn reads "Waiting for a free slot". A basin that has ended reads "Finished", with its years.

3. Wait until the page says that every basin has finished.

## Read the table of the run

When every basin has finished, the page shows the table of the run, with one row for each basin.

| Column | What it shows |
|---|---|
| **Basin** | the code and the name of the basin, with a button **Results** |
| **State** | the state of the basin at the end, such as "Finished" |
| **Run time** | the time that the basin took |
| **Memory** | the peak memory of the engine |
| **Output** | the size of the output tables of the basin |

--8<-- "include/shots/s11_3_table.html"

Click the row of a basin. **Run details** under the table then shows that basin: its number of threads, its years and its warm-up, and the size of the copy of the model.

Click **Results** in a row to open that basin in the **Results** view. There, the box **Basin** chooses the basin to show.

## Save the table

SWATrust writes the table of the run to the file `basins.csv` in the folder of the run, with one line for each basin under a line of column names. [File reference](files.md) says what a line of the file gives. Above the table stands the button **Save the table (CSV)**.

```text
~/SWATrust/runs/
    run_<date>_<time>/
        basins.csv
        run.json
        02070002/
        12110207/
        ...
```

## Video

--8<-- "include/slots/11_run_many.html"

## Next

- [Calibrate and validate](calibrate.md) fits a basin to measured flow.
- [Find the outputs](outputs.md) shows the folder of a run.
