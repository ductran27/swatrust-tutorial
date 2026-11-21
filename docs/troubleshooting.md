# Messages and troubleshooting

This page lists the messages of SWATrust that stop a start or a run, with what each means and what you can do.

## The launcher does not start

### The terminal says "Permission denied"

The copy of the folder lost the mark that lets the two programs run.

What to do: type `chmod +x swatrust swatrs` in the SWATrust folder and start it again.

### The C library (glibc) on Linux

The SWATrust launcher runs on Linux, macOS and Windows. On Linux, the engine needs glibc 2.34 or newer, for example Debian 12, Ubuntu 22.04 or RHEL 9, or newer.

What to do: use a newer system.

### The launcher stops and asks for `--runs`

It found no home folder to make its runs folder in, or it cannot write in the runs folder.

What to do: start it with `--runs` and a folder that you can write in.

### The launcher says that another one already uses the runs folder

A launcher that was started earlier is still running.

What to do: use the page of the first one, or stop the first one with ++ctrl+c++. A second launcher needs a runs folder of its own: start it with `--runs`.

### The launcher says that the engine was not found

The file `swatrs` is not in the folder of the launcher.

What to do: put `swatrs` into the same folder as `swatrust`, or start the launcher with `--engine` and the path of the engine.

## The page does not open or gets no answer

### No browser opens

The computer has no screen, or no default browser.

What to do: copy the address that the launcher printed into a browser.

### The page shows only a short text that asks for the address the launcher printed

The address was typed without its key.

What to do: use the whole address, with the part after `?t=`.

### The page says that the launcher is not running

The terminal was closed, or the launcher was stopped.

What to do: start the launcher again and reload the page; the runs are listed again.

## A folder that is not a model

The dialog **Add a model folder** says "No model in this folder or in the two levels below it: a model folder holds file.cio." The folder you chose holds no SWAT+ model.

What to do: choose the folder that holds the model's `file.cio`.

## A model is refused in Set-up

SWATrust reads a model before any run. A model that this version cannot run is refused there, with one sentence. The sentence starts with "The engine does not run this model in this version:".

For some basins of the published data set, SWATrust knows before the download that this version does not run the basin. The list of basins under the map of **Set-up** shows such a basin with the mark "not run". When you click its row, the line under the list says "This version does not run it:" and gives the reason.

The reasons fall into three groups.

### A part of SWAT+ that this version does not include

Most refusals end with the same words: "it uses a part of SWAT+ that this version does not include." The model turns on a part of SWAT+ that this version does not have. Examples of such parts: pesticides, pathogens, metals, salts or other constituents; the gwflow groundwater module; Green-Ampt infiltration; soft calibration.

What to do: the model cannot be run with this version. The refusal writes nothing into the model folder.

Three kinds of model have a sentence of their own.

#### A decision table that does not fit its header

The sentence says "one of its decision tables (`<file>`) does not match the sizes its header declares", and what follows from it. The header of a decision table gives the numbers of its conditions, alternatives and actions. One table of the named file has lines that do not fit these numbers.

What to do: set the header or the lines of the table right in the model folder and read the model again.

#### An object that receives water from more objects than this version takes

The sentence says "its channel `<name>` receives water from `<n>` objects, more than this version takes for one object." One object of the model receives water from more objects than this version takes. The object is a channel, an outlet, a reservoir or an aquifer.

What to do: the model cannot be run with this version.

#### A management schedule with a decision table that this version cannot run

The sentence says "one of its management schedules runs a decision table (lum.dtl) with a condition on the plants' above-ground biomass, which this version does not include yet." A schedule of `management.sch` starts an operation by a decision table of `lum.dtl`, and the table uses a condition or an action that this version does not have.

What to do: the model cannot be run with this version. One sentence of this kind says that `lum.dtl` does not have the table that a schedule names: correct the name in `management.sch`, or add the table to `lum.dtl`, and read the model again.

### A file of the model that is missing or does not fit

#### A model that the engine could not read

You see "The engine could not read this model. One of its files is missing, cannot be read, or does not match the others." The engine stopped while it read the files of the model. An example: a record that one file names is not in the other file.
What to do: mend the file in the model folder and read the model again.

#### A point-source file that is missing or holds no data

Set-up shows a line such as "No inflow at 1 inlet". `recall.rec` names a point-source file that is not in the model folder or holds no data. Such a file brings the water of a basin upstream. When the inlet has no other source of flow, the run takes no inflow at that inlet, 0 on each day.

What to do: put the file, with its data, into the model folder. For a basin of the data set, [Get a model](models.md#the-flow-from-upstream) shows how the launcher downloads the inflow.

### Output tables that this version does not write

The list **Output tables** in Set-up shows such a table as a row whose boxes cannot be ticked. The run leaves these tables out and writes every other table.

## A period is refused

Set-up or **Start the run** refuses a period that the model cannot run, before any run, and names the years that can be typed. Type a year in the range that the sentence names. [Run streamflow](run-streamflow.md#years-the-page-refuses) shows the three cases: a first year before the model's weather, a last year before the first, and a warm-up that leaves no year to write to the tables.
A fourth case comes from the point-source files of the model: a first year after the year in which they end. The inflow file of an inlet is such a file unless another source gives the inflow of that inlet for every day of the run. Where the model of the basin upstream does so, a first year after the end of the inflow file is not refused. The model 07010206, downloaded with inflow from upstream, cannot start after 2003, because one of its inflow files ends in 2003. Set-up shows the sentence under the year boxes, and **Start the run** gives the same one: "The first year, 2004, is after the model's point-source files, which end in 2003. Choose a first year from 1980 to 2003." It is the same with or without the model 07010207 in the list **Models**, since this version does not run that model. Type a first year in the range that the sentence names. A run of 07010206 that starts in 2003 or earlier takes no inflow from 07010207 after 9 September 2003, the last day of that file.

## Not enough disk space

Before a start, SWATrust reckons the size of the copy of each model and of the output tables. A run that does not fit on the disk of the runs folder, beside the space that SWATrust keeps free, is refused, with the sizes.

What to do: untick tables in Set-up, above all the daily tables of every channel; shorten the period; free some space on the disk; or start the launcher with `--runs` on a larger disk.

A run that fills the disk while it runs is stopped. Its row says "for lack of disk space".

## A run stops with an error

The line of the basin in the run table gives the state and one sentence. The engine's own lines are in the file `engine_main.err` in the folder of the basin in the run folder.

- **Failed**: The engine stopped before the end of the run.
- **Stopped**: The run was ended with the Stop button, or for lack of disk space.
- **Interrupted**: The launcher was closed while the run went.

**Run details**, under the run table, shows the sentence of a basin: at once in a run of one basin, and after a click on the basin's row in a run of several.

## A name with other letter case

Models made on Windows can name a point-source file in lower case and store it in upper case. On a disk that keeps letter case the two names are two files. SWATrust takes care of this in its copy of the model: the copy holds each such file under the name the model asks for, and the run writes nothing into the model folder.

One case stops a run. `recall.rec` names a point-source file that is not in the model folder by that name, and the folder holds two or more files whose names differ from it only in letter case. SWATrust cannot tell which file to read. Set-up shows a box "Letter case" with the names.

What to do: keep only one of these files in the model folder, under the name that `recall.rec` gives.

## Video

--8<-- "include/slots/17_troubleshooting.html"
