# Install and start SWATrust

This page shows how to start SWATrust and stop it, where it keeps its runs, and how to use it on a computer that you reach through `ssh`.

The SWATrust launcher runs on Linux, macOS and Windows. This tutorial is written for Linux.

## What you need

SWATrust needs nothing installed. The launcher, the engine, the maps and one basin are in its folder.

| | |
|---|---|
| A computer | Linux on an x86-64 processor |
| A web browser | the one you already use |
| Disk space | room for the SWATrust folder and for the runs |

The engine needs a Linux with the GNU C library (glibc) 2.34 or newer.

Each run holds a copy of its model and the output tables. Before each run, the page gives the disk space that the run needs and the free space of the disk, under **Checks before the run**.

## The SWATrust folder

[Download](download.md) names the package and says how to unpack it. The unpacked folder is named `SWATrust-linux-x86_64`.

| In the folder | What it is |
|---|---|
| `swatrust` | the launcher: it shows the page and starts the runs |
| `swatrs` | the engine: it runs a SWAT+ model |
| `swatrust_maps.pack` | the maps that the page draws |
| `README.txt`, `LICENSE` | a short guide, and the license of the program |

SWATrust does not write into this folder.

## Start SWATrust

1. Open a terminal and go to the SWATrust folder.

    ```bash
    cd ~/SWATrust-linux-x86_64
    ```

2. Start the launcher.

    ```bash
    ./swatrust
    ```

3. Read what the launcher prints.

    ```text
    SWATrust launcher 1.0.0
      engine:  /home/user/SWATrust-linux-x86_64/swatrs (Linux x86-64)
      runs in: /home/user/SWATrust/runs
      lists:   models.json and history.json in the runs folder
      maps:    /home/user/SWATrust-linux-x86_64/swatrust_maps.pack (… basins)
      open:    http://127.0.0.1:52811/?t=4f0c...
    Keep this window open while you use the launcher. Ctrl-C stops it and any run it started.
    ```

    | Line | What it gives |
    |---|---|
    | `engine` | the engine that the launcher starts for a run |
    | `runs in` | the runs folder, the one place where SWATrust writes |
    | `lists` | the two files that list your models and your runs |
    | `maps` | the file of the maps |
    | `open` | the address of the page |

4. The launcher opens the address in your browser. If no browser opens, copy the whole address from the terminal into your browser.

    Without `--port`, the launcher takes a free port, so the number after `127.0.0.1:` is one that you read from the terminal.

5. Keep the terminal open while you work.

The first start makes the runs folder, `SWATrust/runs` in your home folder. The page then shows an empty list of models, which reads "No model yet". [Quick start](quick-start.md) goes on from there.

If the terminal says "Permission denied", the copy of the folder lost the mark that lets the two programs run. Type the following line and start again.

```bash
chmod +x swatrust swatrs
```

!!! note "The address holds a key"
    The part after `?t=` is a key, and SWATrust makes a new one at each start. A page opened without the key shows two sentences and nothing else: "This page needs the address the launcher printed in its window (it holds a key). Open that address again." and "This address may belong to another SWATrust launcher on this computer. Open the address the launcher you started has printed."

## Stop SWATrust

Press ++ctrl+c++ in the terminal. SWATrust answers `swatrust: stopped.` If a run is going, it first prints `swatrust: stopping 1 engine run(s) it started ...`.

The last line that the launcher prints at its start says the same: "Ctrl-C stops it and any run it started."

Your runs stay in the runs folder.

A run that was going when the launcher stopped is listed after the next start. The tab **Last run** of **Run** then gives its basin the state "Interrupted" and reads "0 of 1 basin finished, 1 interrupted."; under **Run details**, the page says "The run did not reach its end." and "the launcher was closed during the run".

## Choose where SWATrust keeps its runs

SWATrust keeps its runs in its runs folder. Without a choice of yours, that is the folder `SWATrust/runs` in your home folder. A run does not write into the folder of a model, and SWATrust does not write into its own folder. The **Calibration** page keeps the measured flow of a model in a folder `obs` inside the folder of that model, as [Calibrate and validate](calibrate.md#get-the-measured-flow) shows.

To keep the runs somewhere else, such as on a larger disk, start the launcher with `--runs` and a folder.

```bash
./swatrust --runs /data/SWATrust/runs
```

The line `runs in:` then names that folder. Give the same line at every start.

The runs folder also holds the list of your models and the list of your runs.

## Reach SWATrust on another computer

You can run SWATrust on a computer that you reach through `ssh`, such as a workstation or a server, and use the page in the browser of your own computer. The launcher answers only on the computer it runs on, so the page comes to you through `ssh`.

1. On the remote computer, start the launcher with a port of your choice.

    ```bash
    ./swatrust --port 8800
    ```

    On a computer without a screen the launcher opens no browser. After the seven lines of the start it prints two more.

    ```text
    No screen on this computer, so no browser was opened. Open the address above in a browser here,
    or on your own computer through ssh: ssh -N -L 8800:127.0.0.1:8800 <this computer>, then open the address there.
    ```

2. On your own computer, open a terminal and type the `ssh` line, with the name of the remote computer in place of `<this computer>`.

    ```bash
    ssh -N -L 8800:127.0.0.1:8800 <this computer>
    ```

3. Open the address that the launcher printed in the browser of your own computer.

With `--no-open`, the launcher prints the address and does not try to open a browser.

```bash
./swatrust --no-open --port 8800
```

## Video

--8<-- "include/slots/03_install.html"

## Next

- [Quick start](quick-start.md) runs one basin, 02070002 (North Branch Potomac).- [The command line](command-line.md) lists every option of the launcher.
