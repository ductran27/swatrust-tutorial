# The command line

This page lists the options of the SWATrust launcher and shows how to run the engine by hand.

SWATrust has two programs in one folder. The launcher, `swatrust`, shows the page in your browser and starts the runs. The engine, `swatrs`, runs a SWAT+ model and writes its output tables. You start the launcher; the launcher starts the engine.

## Start the launcher

```text
./swatrust
```

On Windows, in PowerShell, type `.\swatrust.exe` in place of `./swatrust`.

[Install and start SWATrust](install.md#start-swatrust) shows the start step by step.

## Options of the launcher

| Option | What it does | Without it |
|---|---|---|
| `--runs <folder>` | names the runs folder, where runs and lists are written | `SWATrust/runs` in your home folder, made at the first start |
| `--port <n>` | serves the page on the port you give | a free port |
| `--no-open` | prints the address and opens no browser | the launcher opens your browser |
| `--engine <path>` | names an engine that is not beside the launcher | the engine in the launcher's folder |
| `--version` | prints the version and stops | |
| `--tile-share <model folder>...` | prints each model's tile share and whether the tile pair is searched, and starts nothing | |

## A computer without a screen

With `--no-open` and `--port` the launcher runs on a computer that you reach through `ssh`. [Install and start SWATrust](install.md#reach-swatrust-on-another-computer) shows the steps.

## The engine

The launcher writes the command line of each engine run into the run folder, in the file `engine_main.args` of the basin. The file holds one word on each line. For the run of [Run streamflow](run-streamflow.md) the words, put on one line, read as follows.

```text
run --threads 1 --out-dir ~/SWATrust/runs/run_<date>_<time>/02070002/out ~/SWATrust/runs/run_<date>_<time>/02070002/TxtInOut
```

| Part | Meaning |
|---|---|
| `run` | run the model |
| `--threads N` | the number of threads inside the model; one thread without the option |
| `--out-dir <folder>` | the folder for the output tables |
| the last part | the model folder to run: here the copy that SWATrust made |

### Run the engine by hand

The engine runs one model without the launcher. Give it a folder for the output tables and the model folder. Without `--out-dir` the engine writes no table.

The copy that SWATrust made for a run, `TxtInOut` in the folder of the basin, is a model folder that the engine can run again. The line below runs it and writes the tables into a folder of your choice. The engine makes the output folder if it is not there, and says on the screen when the run is complete.

```text
./swatrs run --out-dir ~/my_tables ~/SWATrust/runs/run_<date>_<time>/02070002/TxtInOut
```
