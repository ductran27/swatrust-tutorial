# Run sediment

This page shows how to read the sediment of a run in three places: the land, the channels and the basin outlet.

The run of this page is the run of [Run streamflow](run-streamflow.md): the basin 02070002, 2000 to 2015, with a warm-up of three years. The page draws no chart of sediment, so this chapter reads the tables of the run folder.

## The tables of this chapter

The run of [Run streamflow](run-streamflow.md) already wrote the three files of this chapter. No new run is needed.

| Where | Row of **Output tables** in Set-up | File | Column | Unit |
|---|---|---|---|---|
| The land | Entire basin, Sediment and nutrients, Year | `basin_ls_yr.txt` | `sedyld` | t/ha |
| The channels | Channels, Every channel, Year | `sd_chanbud_yr.txt` | `bank_ero`, `ch_dep`, `fp_dep` | t |
| The outlet | no row: the model's file object.prt asks for it | `020700020803_con.out` | `sed` | t a day |

Here t is the metric ton.

--8<-- "include/shots/s09_1_ticks.html"

## Sediment that leaves the land

The column `sedyld` of `basin_ls_yr.txt` is the sediment yield of the land: the sediment that leaves the land of the basin in a year, in t/ha. The same column of `hru_ls_yr.txt` gives it for each HRU.

SWAT+ computes the sediment yield of an HRU on each day with surface runoff. Its source code (file `ero_ysed.f90`, routine `ero_ysed`) computes it as

\[
sed = 11.8 \times \left(10 \times Q_{surf} \times q_{peak} \times A\right)^{0.56} \times K \times C \times P \times LS \times CFRG
\]

where \(sed\) is the sediment yield of the day (t), \(Q_{surf}\) is the surface runoff of the day (mm), \(q_{peak}\) is the peak runoff rate (m³/s), \(A\) is the area of the HRU (ha), \(K\) is the erodibility factor of the first soil layer, \(C\) is the cover factor of that day, \(P\) is the support practice factor, \(LS\) is the topographic factor, and \(CFRG\) is the coarse fragment factor. One mm of water over one ha is 10 m³, so \(10 \times Q_{surf} \times A\) is the volume of the day's runoff in m³.

The coarse fragment factor is computed from the rock content of the first soil layer:

\[
CFRG = \exp(-0.053 \times rock)
\]

where \(rock\) is the rock content (%). SWAT+ computes \(C\) each day with runoff from the residue on the surface and the above-ground plant mass. On a day without surface runoff the yield is 0.

## The sediment budget of the channels

The table `sd_chanbud` holds the sediment budget of every channel. Each line is one channel and one year, and each column is the sum of the channel's daily amounts in t.

| Column | Holds |
|---|---|
| `bank_ero` | sediment eroded from the banks of the channel |
| `ch_dep` | sediment deposited in the channel |
| `fp_dep` | sediment deposited on the flood plain |

## Sediment at the basin outlet

The record of the basin outlet, `020700020803_con.out`, holds the sediment that passes the outlet on each day in its column `sed`, in t. The record holds every simulated day, the warm-up years too.

## The three side by side

The following lines add up each of the three for every printed year. They use `read_table` and `read_record` of [Read the results](read-results.md#read-a-table-with-your-own-program).

```python
AREA_HA = 350343.2   # land area of the model, from its file object.cnt

land = {}
for row in read_table("basin_ls_yr.txt"):
    land[row["yr"]] = float(row["sedyld"]) * AREA_HA

bank = {}
deposition = {}
for row in read_table("sd_chanbud_yr.txt"):
    year = row["yr"]
    bank[year] = bank.get(year, 0.0) + float(row["bank_ero"])
    deposition[year] = deposition.get(year, 0.0) + float(row["ch_dep"]) + float(row["fp_dep"])

outlet = {}
for row in read_record("020700020803_con.out"):
    year = row["yr"]
    outlet[year] = outlet.get(year, 0.0) + float(row["sed"])

print("year land banks deposition outlet")
for year in sorted(land):
    print(year, round(land[year]), round(bank[year]), round(deposition[year]), round(outlet[year]))
```

The land area of the model stands in the column `LS_AREA` of its file `object.cnt`, in ha. The yield of the land in t/ha times this area is the sediment that leaves the land in t.

```text
year land banks deposition outlet
2003 33283 2124803 784896 1327580
2004 22772 1933637 586676 1352786
2005 15065 1797804 494602 1307578
2006 9810 1725590 372217 1350026
2007 12612 1713010 410393 1302178
2008 21371 1899949 603657 1298404
2009 16816 1769121 445227 1327702
2010 19269 1735800 448191 1291618
2011 26626 1978223 669066 1313216
2012 11211 1726533 377674 1346733
2013 15415 1779576 443797 1335039
2014 16116 1752966 427803 1327090
2015 12612 1699024 383548 1316669
```

In this run the channel budget table shows that most of the sediment at the outlet comes from the banks of the channels.

The three sums are not a budget of the basin. The reservoirs of the model keep part of the sediment that enters them, and no column of the channel table holds that part. The table `reservoir_yr.txt` gives the sediment that enters and that leaves each reservoir in its columns `sed_in` and `sed_out`, in t.

## References

Neitsch, S.L., Arnold, J.G., Kiniry, J.R., Williams, J.R., 2011. Soil and Water Assessment Tool theoretical documentation, version 2009. Texas Water Resources Institute Technical Report No. 406. Texas A&M University System, College Station, Texas.

## Video

--8<-- "include/slots/09_run_sediment.html"

## Next

- [Run water quality](run-water-quality.md) reads the nutrients of the same run.
- [File reference](files.md) lists the head lines and the columns of the tables.
