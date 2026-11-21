# Download

This page says what to download for the tutorial and how to unpack it.

You need one file for the first chapters: the SWATrust package for your computer. The launcher then downloads the basin of the first run when you ask for it.

!!! note "Before you start"
    The SWATrust launcher runs on Linux, macOS and Windows. The steps of this page were done on Linux, on macOS and on Windows.

## What to download

| File | Holds |
|---|---|
| `SWATrust-linux-x86_64.tar.gz` | SWATrust for Linux on x86-64 processors |
| `SWATrust-macos-arm64.tar.gz` | SWATrust for macOS on Apple silicon |
| `SWATrust-windows-x86_64.zip` | SWATrust for Windows on x86-64 processors |

Download the package of your computer from [the Releases page of the tutorial's repository](https://github.com/ductran27/swatrust-tutorial/releases).

### The published models

The launcher downloads a basin of the published data set (Tran, 2026) when you ask for it. You do not need to download that data set yourself; [Get a model](models.md) shows the way through the launcher. The address of the data set is https://doi.org/10.6084/m9.figshare.35018494.

## Unpack the package

1. Open a terminal in the folder that holds the downloaded file. On macOS, the terminal is the Terminal app; on Windows, it is PowerShell.

2. Unpack the package.

    ```
    tar -xzf SWATrust-linux-x86_64.tar.gz
    ```

    The folder `SWATrust-linux-x86_64` appears beside the file.

    On macOS:

    ```
    tar -xzf SWATrust-macos-arm64.tar.gz
    ```

    The folder `SWATrust-macos-arm64` appears beside the file.

    On Windows:

    ```
    tar -xf SWATrust-windows-x86_64.zip
    ```

    The folder `SWATrust-windows-x86_64` appears beside the file.

The folder holds the whole program:

| In the folder | What it is |
|---|---|
| `swatrust` | the launcher; the page you work on is inside it |
| `swatrs` | the SWATrust engine |
| `swatrust_maps.pack` | the maps of the basins |
| `README.txt`, `LICENSE` | a short guide, and the license of the program |

On Windows, the launcher and the engine are `swatrust.exe` and `swatrs.exe`.

## What SWATrust does not do here

- Nothing is installed. The unpacked folder is the program.
- The launcher downloads nothing by itself. It uses the network only when you press a **Download** button.

## References

Tran, D. (2026). SWATrust: SWAT+ input files for HUC8 basins of the conterminous United States [Dataset]. figshare. https://doi.org/10.6084/m9.figshare.35018494

## Next

[Install and start SWATrust](install.md) starts the launcher from the unpacked folder.

<p class="checked">Checked on SWATrust launcher 1.0.0, the Linux x86-64 package, the macOS package for Apple silicon and the Windows x86-64 package, on 21 November 2026.</p>
