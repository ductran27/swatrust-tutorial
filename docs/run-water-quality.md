# Run water quality

This page shows how to read the nitrogen and the phosphorus that leave the land in a run, and where the run writes the loads at the basin outlet.

The run of this page is the run of [Run streamflow](run-streamflow.md): the basin 02070002, 2000 to 2015, with a warm-up of three years. The page draws no chart of nutrients, so this chapter reads the tables of the run folder.

## The tables of this chapter

The run of [Run streamflow](run-streamflow.md) already wrote the tables of this chapter by month, by year and for the average year.

| Row of **Output tables** in Set-up | Table | What it holds |
|---|---|---|
| Entire basin, Sediment and nutrients | `basin_ls` | nutrients that leave the land, mean over the basin's land |
| HRUs, Sediment and nutrients | `hru_ls` | the same for each HRU |
| Entire basin, Nutrient balance | `basin_nb` | gains of the land and transfers between the soil's pools |

--8<-- "include/shots/s10_1_ticks.html"

Every value of these tables is an amount for one ha of land in the step of the table: kg of nitrogen (N) or kg of phosphorus (P) per ha. The units line of the files prints `kgha`.

## Nutrients that leave the land

The table `basin_ls` gives the ways by which nitrogen and phosphorus leave the land.

| Column | Holds | Unit |
|---|---|---|
| `surqno3` | nitrate carried in surface runoff | kg N/ha |
| `lat3no3` | nitrate carried in lateral flow | kg N/ha |
| `tileno3` | nitrate in tile flow | kg N/ha |
| `sedorgn` | organic nitrogen carried with sediment in surface runoff | kg N/ha |
| `surqsolp` | soluble phosphorus carried in surface runoff | kg P/ha |
| `sedorgp` | organic phosphorus carried with sediment in surface runoff | kg P/ha |
| `sedminp` | mineral phosphorus carried with sediment | kg P/ha |
| `lchlabp` | soluble phosphorus that leaches below the soil profile | kg P/ha |

The head of each table of the entire basin ends with names that have no values in its lines: `plant_cov` and `mgt_ops` in `basin_wb`, `basin_nb`, `basin_ls` and `basin_pw`, and `percn` too in `basin_ls`. These columns have values in the tables of the HRUs only. The average-year line of `basin_wb` is the one exception: it ends with words that belong to no column.

SWAT+ defines these columns in its source file `output_landscape_module.f90`.

## The nutrient balance of the land

The table `basin_nb` gives what the land gains and what the plants take up.

| Column | Holds | Unit |
|---|---|---|
| `fertn`, `fertp` | nitrogen and phosphorus applied to the soil | kg N/ha, kg P/ha |
| `grzn`, `grzp` | nitrogen and phosphorus added to the soil by grazing animals | kg N/ha, kg P/ha |
| `fixn` | nitrogen fixation | kg N/ha |
| `no3atmo`, `nh4atmo` | nitrate and ammonium (as N) deposited from the atmosphere | kg N/ha |
| `nuptake`, `puptake` | nitrogen and phosphorus taken up by plants | kg N/ha, kg P/ha |
| `denit` | nitrogen lost from the nitrate of the soil by denitrification | kg N/ha |

The other columns of the table give the amounts that move from one pool of the soil to another. The head line of the file names every column, as [File reference](files.md#the-output-tables) describes.

## Read the yearly values

The following lines print the losses and the gains of each printed year. They use `read_table` of [Read the results](read-results.md#read-a-table-with-your-own-program).

```python
print("year surqno3 lat3no3 tileno3 sedorgn | surqsolp sedorgp sedminp")
for row in read_table("basin_ls_yr.txt"):
    print(row["yr"], row["surqno3"], row["lat3no3"], row["tileno3"], row["sedorgn"], "|",
          row["surqsolp"], row["sedorgp"], row["sedminp"])

print("year fertn fixn no3atmo nh4atmo nuptake denit")
for row in read_table("basin_nb_yr.txt"):
    print(row["yr"], row["fertn"], row["fixn"], row["no3atmo"], row["nh4atmo"], row["nuptake"], row["denit"])
```

```text
year surqno3 lat3no3 tileno3 sedorgn | surqsolp sedorgp sedminp
2003 1.782 0.264 0.009 0.230 | 0.082 0.029 0.063
2004 0.673 0.313 0.002 0.149 | 0.042 0.019 0.042
2005 0.887 0.321 0.002 0.092 | 0.033 0.012 0.026
2006 0.343 0.424 0.001 0.040 | 0.021 0.006 0.011
2007 0.734 0.331 0.000 0.074 | 0.034 0.010 0.020
2008 1.375 0.330 0.003 0.140 | 0.057 0.018 0.038
2009 0.733 0.236 0.000 0.109 | 0.045 0.014 0.030
2010 0.775 0.241 0.002 0.143 | 0.055 0.018 0.040
2011 0.777 0.326 0.003 0.143 | 0.068 0.018 0.043
2012 0.366 0.353 0.001 0.064 | 0.022 0.008 0.018
2013 0.998 0.319 0.000 0.091 | 0.049 0.011 0.026
2014 0.679 0.176 0.000 0.129 | 0.052 0.016 0.032
2015 0.604 0.243 0.000 0.067 | 0.045 0.009 0.020
year fertn fixn no3atmo nh4atmo nuptake denit
2003 8.846 0.091 7.033 1.081 33.525 0.011
2004 11.256 0.165 5.774 0.932 33.407 0.012
2005 8.846 0.043 5.884 0.835 29.151 0.011
2006 11.256 0.133 5.277 0.913 32.345 0.014
2007 8.846 0.081 5.692 0.926 31.281 0.013
2008 11.256 0.167 5.246 1.139 31.130 0.019
2009 8.846 0.057 4.128 1.047 29.845 0.010
2010 11.256 0.119 4.843 0.997 31.365 0.008
2011 8.846 0.070 4.422 1.242 30.843 0.018
2012 11.256 0.160 3.851 1.169 32.013 0.014
2013 8.846 0.072 3.702 1.148 31.747 0.013
2014 11.256 0.171 3.734 1.127 32.978 0.008
2015 8.846 0.076 3.711 1.063 32.506 0.008
```

To find the HRUs that lose the most, read `hru_ls_yr.txt` the same way: it has one line for each HRU and year. Its columns `plant_cov` and `mgt_ops` name the plant cover and the management of the HRU, and its column `percn` gives the nitrate that leaches from the bottom of the soil profile, in kg N/ha.

The following lines print the five HRUs that lose the most nitrate in surface runoff in 2010, with their nitrate that leaches, their plant cover and their management.

```python
rows = [row for row in read_table("hru_ls_yr.txt") if row["yr"] == "2010"]
rows.sort(key=lambda row: float(row["surqno3"]), reverse=True)
for row in rows[:5]:
    print(row["name"], row["surqno3"], row["percn"], row["plant_cov"], row["mgt_ops"])
```

```text
163519 11.402 32.474 fesc past_cmz_04.1__dry_100112
163521 11.402 32.474 fesc past_cmz_04.1__dry_100112
163522 11.402 32.474 fesc past_cmz_04.1__dry_100112
141978 8.690 12.156 fesc past_cmz_04.1__dry_100111
141979 8.690 12.156 fesc past_cmz_04.1__dry_100111
```

## Loads at the basin outlet

The record of the basin outlet, `020700020803_con.out`, holds the loads that pass the outlet on each day.

| Column | Holds | Unit |
|---|---|---|
| `orgn` | organic nitrogen | kg N a day |
| `no3` | nitrate | kg N a day |
| `nh3` | ammonia | kg N a day |
| `no2` | nitrite | kg N a day |
| `sedp` | organic phosphorus | kg P a day |
| `solp` | soluble phosphorus | kg P a day |
| `chla` | chlorophyll-a | kg a day |
| `cbod` | carbonaceous biological oxygen demand | kg a day |
| `dox` | dissolved oxygen | kg a day |

SWAT+ defines these columns in its source file `hydrograph_module.f90`. [Find the outputs](outputs.md#the-record-of-an-outlet) shows where the record lies, and [File reference](files.md#the-records-of-objectprt) lists all its columns.

## Parts that this version does not include

This version of SWATrust does not include every part of SWAT+. A model that uses a part it does not include is not run, and the **Set-up** page says so. [Messages and troubleshooting](troubleshooting.md) lists the messages.

## Video

--8<-- "include/slots/10_run_water_quality.html"

## Next

- [Run several basins](run-many.md) runs more than one basin in one go.
- [File reference](files.md) lists the head lines and the columns of the tables.
