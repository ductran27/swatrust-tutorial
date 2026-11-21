# Calibrate and validate

This page shows how to fit the parameters of a model to the flow measured at its outlet, and how to check the fitted model on years that it was not fitted to.

## What you need

- A model in **Set-up**. This page uses the basin 01020003.
- The flow measured at a point of the model, one value for each day. This page uses the daily values of the gauge 01030500 of the U.S. Geological Survey (USGS), "Mattawamkeag River near Mattawamkeag, Maine". The Calibration page gets these values from USGS when you click **Download**, so the computer needs a connection to the internet for that step. A file of your own can be given instead. The record is cited under [References](#references).

## Open the Calibration page

1. In **Set-up**, click **Clear choice** and tick the model 01020003, so that it is the only model chosen.
2. Click **Calibration**, the fourth of the four views. The box **Model** names the model.
3. In the bar **Method**, leave **DDS**. DDS is the page's name for its search, which [Set the number of simulations](#set-the-number-of-simulations) describes.

## Get the measured flow

Under **Measured data**, the row of the measured flow has three parts: **Variable**, which reads "Streamflow", **Where** and **Measured file**. Under **Measured file**, the page names the gauge of the model, "This HUC uses USGS 01030500, Mattawamkeag River near Mattawamkeag, Maine", and has the button **Download** under that line. Until the page has a measured flow, it reads "Choose the measured flow." under **Checks**.

1. Click **Download**.

The page says of the gauge: "Download asks USGS for the days of this gauge in the model's years, writes them into the folder obs of the model and reads them." Under the button, the page names those days: "Asks for the days from 1997-01-01 to 2025-12-31." While the page waits for the answer, the button is off and the page reads "asking USGS…". USGS gives its values in cubic feet per second. The downloaded file holds each day in cubic feet per second and in m³/s, and the page reads the column in m³/s.

The page then counts the days of the file and of each period.

| What the page shows | In the walk of this page |
|---|---|
| the days in the file | 10,592 days, 1997-01-01 to 2025-12-31, in m³/s |
| **Days measured** and **Days missing** in the calibration years | 4,749 and 0 |
| **Days measured** and **Days missing** in the validation years | 4,748 and 0 |
| **USGS estimated** in the calibration and in the validation years | 1,406 and 1,453 |

The page says of the column **USGS estimated**: "days for which USGS gives an estimated flow, not a measured one".

The file stays in the folder `obs` of the model, and the page reads it when you open **Calibration** for the model again. When that file ends before the last year of the model, a line under the gauge gives the days the file was kept for and the years the model now reaches, and ends "Download asks USGS for those days."

The page compares the measured flow with the daily flow of one channel of the model. The menu **Where** names that channel. The page says of the menu: "The channel of the model whose daily flow is compared with the measured flow. The launcher sets it for a gauge it lists. With a file of your own or another station, choose it." It adds that the words "basin outlet" mark "a place where the water leaves the model". For this model the menu holds "Channel 1222 (at the gauge)". In this model, the drainage area of that channel is within a tenth of a percent of the drainage area of the gauge.

--8<-- "include/shots/s12_1_file.html"

The page also has a band **USGS gauges**, which shows the gauges as marks on a map of the conterminous United States. The page says of the map: "A mark is a USGS gauge whose daily flow can be compared with a model of the data set. The basin of the model chosen under "Model" is yellow." The band names the gauge of the model, and it has a button **Download** of its own for that gauge. Over the map, under the label **USGS stations**, are four buttons: **Streamflow**, **Suspended sediment**, **Nitrogen** and **Phosphorus**. The page says of them: "A button of "USGS stations" shows the stations with data of that kind."

--8<-- "include/shots/s12_7_gauges.html"

## A file of your own

The page also reads a file of your own in place of the download. The page says of such a file: "One text file, one day on a line: the date and the flow in m³/s, as in 2000-01-31, 12.4. A day without a number is a missing day." It also reads "a USGS file of daily values in ft³/s, and dates as 01/31/2000 or 20000131".
To give the file through the dialog:

1. Under **Measured file**, click **Choose**. The dialog **Choose a measured flow file** opens.
2. In the box beside **Up**, type the path of the folder that holds the file and press ++enter++. The list shows the files of the folder.
3. Click the file. Its name stands at the foot of the dialog.
4. Click **Use this file**.

The path of the file may also be typed in the box under **Measured file**, followed by ++enter++.

SWATrust copies the file into the folder `obs` of the model's folder, and the box then holds the path of the copy.

The file is a text file with one day on each line: a date and a flow in m³/s.

```text
date,flow_m3s
1997-01-01,104.772332
1997-01-02,96.8436153
1997-01-03,93.4455938
```

- The date is written as `2010-01-31`, `2010/01/31`, `01/31/2010` or `20100131`. For a date such as `01/31/2010`, the page adds the line "Dates month/day/year".
- The columns are split by a tab, a comma, a semicolon or spaces.
- A line that starts with `#` is skipped. A first line of column names is skipped too.
- A day without a measurement has an empty flow or `NA`, or is left out of the file.
- When the file has more than two columns, the "i" beside **Measured file** names the column that the page reads the flow from, as in "Flow from column 2 (flow_m3s)."
- A negative flow is refused, so a value such as -999 cannot mark a missing day.

With a file of your own, **Checks** reads "Choose the channel under Where." and **Start the calibration** is off until a channel is chosen in **Where**.

The page tells you when it cannot read a file. **Checks** then reads "Measured flow unreadable; see above."

- A file that has a negative flow: "Line 64: the flow -999 is negative. A day without a measurement is marked by an empty flow or NA, or left out of the file."
- A file that has no line with a date and a flow: "The file lists no day with a flow (one line per day: a date and a flow in m3/s)."
- A file that is not at the place given: "The measured file is not there", with the path.

## Set the three periods

A calibration divides the years of the model into three periods.

| Period | What happens in it |
|---|---|
| Warm-up | the model runs to settle; these years are not scored |
| Calibration | the search scores each set of parameter values on these years |
| Validation | years the search does not use; they test the fitted values |

The page opens with periods of its own, and the boxes under **Years** hold them: 1997 to 1999 for the warm-up, 2000 to 2012 for the calibration and 2013 to 2025 for the validation. This page uses shorter periods so that the search stays small.

1. Under **Years**, type `2010` and `2010` for the warm-up, `2011` and `2012` for the calibration years, and `2013` and `2014` for the validation years. Press ++enter++ after each year.

The table of the days now gives 731 days measured for the calibration years and 730 for the validation years, with no day missing. Its column **USGS estimated** gives 188 and 229.

--8<-- "include/shots/s12_2_periods.html"

The search scores the calibration years and does not see the validation years. The warm-up years are not scored.

## Choose the parameters and their ranges

The list **Parameters** holds the parameters that the search can change. Each parameter has a lowest and a highest value, and the search stays between them.

The word under the name of a parameter says how a value is applied: "add" adds the number to the model's value, "percent" changes it by that percent, and "replace" replaces it.

| Parameter | Name on the page | Applied as | Lowest | Highest | Ticked as the page opens |
|---|---|---|---|---|---|
| `cn2` | Curve number | add | -10 | 10 | yes |
| `cn3_swf` | Curve number, soil water factor | percent | -50 | 50 | yes |
| `awc` | Available water capacity | percent | -50 | 50 | yes |
| `k` | Soil conductivity, saturated | percent | -50 | 100 | yes |
| `chk` | Channel bed conductivity | percent | -50 | 100 | yes |
| `evrch` | Channel evaporation factor | replace | 0.5 | 1 | yes |
| `alpha` | Baseflow recession constant | replace | 0.01 | 1 | yes |
| `flo_min` | Depth limit of groundwater flow | percent | -95 | 100 | yes |
| `revap_co` | Revap coefficient | replace | 0.02 | 0.2 | yes |
| `revap_min` | Depth limit of revap | replace | 0 | 10 | yes |
| `deep_seep` | Seepage to deeper layers | replace | 0.001 | 0.4 | yes |
| `sp_yld` | Specific yield | replace | 0.01 | 0.4 | yes |
| `k_res` | Reservoir bed conductivity | replace | 0 | 1 | yes |
| `bf_max` | Groundwater flow to reach all channels | replace | 0.1 | 2 | no |
| `slope` | Land slope | percent | -50 | 50 | no |
| `tile_dtime` | Tile drains: time to drain | replace | 0 | 72 | no |
| `tile_drain` | Tile drains: drainage coefficient | replace | 10 | 51 | no |

The column **Initial** gives the value that the model has before the search.

Beside "replace", the row of `alpha` has the words "log scale". The page says of them: "Searched on a log scale: the search spreads its values evenly over the powers of ten between the lowest and the highest value."

The list has a box to tick for each parameter and two boxes for its range. The range of a parameter without a tick shows as plain numbers, without boxes.
To change the list:

1. Click the box of a parameter to set its tick or to take it out.
2. To change a range, type a new value in the box **Lowest** or **Highest** and press ++enter++.

The page checks a value when you press ++enter++. A value that it cannot take is not kept. A line under the parameter then says why, **Checks** reads "A bound is wrong; see Parameters.", and **Start the calibration** is off. The page answered three values of the walk as follows.

```text
Highest "-20": the lowest must be below the highest. Previous value 10 kept.
Highest "2": above 1, the highest allowed. Previous value 1 kept.
Lowest "abc": not a number. Previous value 0.01 kept.
```

A line goes away when you type a value that the page can take into that box. When no line is left, **Start the calibration** is on again.

This page leaves the list as it opens.

--8<-- "include/shots/s12_3_params.html"

### Add a parameter

The list opens with the parameters of the table above. To search a parameter that is not in it, add its name.

1. Click **Add parameter**. A list of names stands in place of the table. Each name has an "i" that gives its group and its limits in `cal_parms.cal`.
2. In **Find a parameter**, type part of a name, such as `canmx`. The list keeps the names that hold the typed part.
3. Click **Add** beside the name. Its line then reads "In the table".
4. Click **Close**. The new row is the last of the table. It is ticked and has a range of its own.
5. To take the row out again, click **Remove** beside its name.

Not every name of the list can be added: some have no button **Add**. Beside some names that have the button, the list reads "Not yet tested against SWAT+".

## Set the number of simulations

The Calibration page calls one run of the model with one set of parameter values a simulation. The search works in iterations. The first simulation uses the initial parameters, the values that the model has before the search. Each iteration after it tries a number of new sets of values around the best set found so far. The search is a batch form of the dynamically dimensioned search (DDS) of Tolson and Shoemaker (2007).

The page says of an iteration: "An iteration is a set of simulations drawn around the best set so far and run in parallel; the best set moves after each iteration. The ranges do not narrow as in SUFI-2."

Two boxes under **Simulations** set the size of the search: **Iterations** and **Simulations per iteration**. The page opens with 15 iterations of 16 simulations. This page uses a small search of 5 iterations of 8 simulations to show the steps.

1. In **Iterations**, type `5` and press ++enter++.
2. In **Simulations per iteration**, type `8` and press ++enter++.

The two final simulations are made after the last iteration: one with the initial parameters and one with the calibrated set.

The page says of a simulation: "A simulation is one model run with one set of values."

## Start and watch

1. Click **Start the calibration**.

    Under **Checks**, the page reads "Running; settings locked.", and the button **Stop** stands in place of the start button.

2. Watch the block **Result**.

    Its head counts the simulations, as in "searching, 9 of 43 simulations". Its table has three lines, one for each step: "Initial simulation", "Iterations 1 to 5" and "Final simulations". Each line gives its simulations and its state: "waiting", "running" or "done". The line of the iterations names the iteration that is running.

    Under the table, the line "Best so far" gives the value of KGE daily for the best set and the iteration that found it, beside its value for the initial simulation.

    The tab **Progress** draws one dot for each simulation and a line through the highest value so far. The line and the chart use KGE daily, which [How a fit is scored](#how-a-fit-is-scored) describes.

The page says of a search: "The calibration goes on in the launcher: the browser tab may be closed and opened again."

--8<-- "include/shots/s12_4_running.html"

## How a fit is scored

SWATrust compares the simulated flow with the measured flow on the days of a period that have a measured flow. It gives three statistics.

The Nash-Sutcliffe efficiency (NSE) of Nash and Sutcliffe (1970), in the form that Gupta et al. (2009) give, is

\[
NSE = 1 - \frac{\sum_{i} (O_i - S_i)^2}{\sum_{i} (O_i - \bar{O})^2}
\]

where \(O_i\) is the measured flow of day \(i\) (m³/s), \(S_i\) is the simulated flow of that day (m³/s), and \(\bar{O}\) is the mean of the measured flows on those days. An NSE of 1 is a perfect fit.

The Kling-Gupta efficiency (KGE) of Gupta et al. (2009) is

\[
KGE = 1 - \sqrt{(r - 1)^2 + (\alpha - 1)^2 + (\beta - 1)^2}
\]

where \(r\) is the correlation of the simulated and the measured flow, \(\alpha\) is the standard deviation of the simulated flow divided by that of the measured flow, and \(\beta\) is the mean of the simulated flow divided by the mean of the measured flow. A KGE of 1 is a perfect fit.

The percent bias (PBIAS) of Moriasi et al. (2007) is

\[
PBIAS = 100 \times \frac{\sum_{i} (O_i - S_i)}{\sum_{i} O_i}
\]

A positive PBIAS means that the simulated flow is lower than the measured flow in the sum.

The page gives the KGE for the daily flows and for the monthly means, and the NSE and the PBIAS for the daily flows. A monthly mean is used only for a month in which every day has a measured flow.

The box **Objective function** names the objective function of the search. As the page opens, it holds "KGE daily": the KGE of the daily flow in the calibration years. This page leaves the objective function as the page opens it. The search looks for the set with the highest value of the objective function.

## Read the result

When the search has ended, the head of **Result** reads "finished, 43 of 43 simulations".

### The calibrated set

The box at the top of **Result** reads "Calibrated". The "i" of the box names the simulation and the iteration that gave the calibrated set, and the gain in KGE daily over the initial parameters.

In the list **Parameters**, the column **Calibrated** gives the value of each ticked parameter in the calibrated set, in the same row as its initial value.

### The statistics

The table **Statistics** has a line "Initial" and a line "Calibrated" for the calibration years and for the validation years. Its columns are "KGE daily", "KGE monthly", "NSE daily" and "PBIAS daily, %".

Compare the two lines of each period. A set that fits the measured flow better has a KGE and an NSE nearer to 1 and a PBIAS nearer to 0. The search did not use the validation years, so their statistics show how the calibrated set predicts flow in years that it was not fitted to.

For some days of the file of this chapter, USGS gives an estimated flow, not a measured one. Above the table, **All days** and **Without estimated days** choose the days on which the two final simulations are scored. The table opens on **All days**. Click **Without estimated days** to see the statistics of the two final simulations on the other days only. The table of the constraints does not change with this choice. The line under it gives the share of the estimated days: "Estimated: 25.7 % of the calibration days, 31.4 % of the validation days."

The table of the constraints stands under the table **Statistics**; its first column has the head **Constraint**. It has four lines: "KGE monthly", "NSE daily", "KGE of 1/Q (low flows)" and "|PBIAS| daily, %". Each line gives the value with the initial parameters, the value with the calibrated set and the bound. Under **Met**, the word "yes" says that the calibrated set meets the constraint. During the search, a set replaces the best set only when it meets the constraints and has a higher value of the objective function.

### The charts

The chart **Daily flow** draws three lines: the measured flow, the flow with the initial parameters and the flow with the calibrated set. It opens on the years after the warm-up, 2011 to 2014 in this chapter. The page says of the chart: "The shaded years are the calibration years." Click **Two years** to see two years at a time; the button then reads **All years**.

--8<-- "include/shots/s12_5_result.html"

In **Result**, the tab **Flow duration** draws the same three flows against a share of the days, from 0 to 100 %, with the flow on a logarithmic scale. The tab **Simulations** lists every simulation of the search by iteration, with its KGE, NSE and PBIAS.
### The two final simulations

To see the two final simulations, click **Open in Results**. SWATrust opens **Results**, and the box **Basin** lists them as "01020003 Mattawamkeag River (unrouted) | Calibrated" and "01020003 Mattawamkeag River (unrouted) | Initial". The heading of the view names the simulation that is shown. The head of **Results** gives the years after the warm-up, 2011–2014.

### The folder of the calibration

SWATrust keeps each calibration in a folder of its own beside the folders of the runs.

```text
~/SWATrust/runs/
    cal_<date>_<time>/
        calibration.cal
```

The file `calibration.cal` holds the calibrated values. [File reference](files.md#calibrationcal-changes-to-parameters) explains its lines. The search does not change the folder of the model.

## Use the fitted values in a run

1. In **Result**, click **Use calibrated values**.

    SWATrust opens **Set-up**. In the block of the model, the line under **Calibrated values** reads "the values a calibration chose, with its files" and gives the path of the file `calibration.cal` in the folder of the calibration.

    --8<-- "include/shots/s12_6_use.html"

2. In **First year**, type `2010` and press ++enter++.
3. In **Last year**, type `2014` and press ++enter++.
4. In **Warm-up**, type `1` and press ++enter++. The line under the boxes begins "5 years, the first as warm-up."
5. Click **Continue to Run**, and then click **Start the run**.
6. When the run has finished, click **See the results**. The head of **Results** reads 2011–2014.

The page says that the button "makes the runs of this model in Set-up take that file".
The run applies the calibrated values to its own copy of the model, and the folder of the model stays as it is. [Read the results](read-results.md) explains the **Results** view. [Change inputs](change-inputs.md#choose-the-calibrated-values) shows how to go back to the model's own values.

## Calibrate another model at the same time

The Calibration page shows one model. To work on a second model without leaving the first, open a tab for it.

1. At the right of the bar **Method**, click **Calibrate another model**. A strip of tabs stands over the page, with one tab for each model, and the new tab shows the other model.
2. Click a tab to see its model.
3. To take a tab away, click the close mark beside its name.

The page says of the tabs: "A tab holds the calibration of one model, and calibrations in different tabs go at the same time." Each parallel simulation of a calibration that is going takes one thread, and the strip counts the threads in use.

## References

Gupta, H.V., Kling, H., Yilmaz, K.K., Martinez, G.F., 2009. Decomposition of the mean squared error and NSE performance criteria: Implications for improving hydrological modelling. Journal of Hydrology 377 (1-2), 80-91.

Moriasi, D.N., Arnold, J.G., Van Liew, M.W., Bingner, R.L., Harmel, R.D., Veith, T.L., 2007. Model evaluation guidelines for systematic quantification of accuracy in watershed simulations. Transactions of the ASABE 50 (3), 885-900.

Nash, J.E., Sutcliffe, J.V., 1970. River flow forecasting through conceptual models part I - A discussion of principles. Journal of Hydrology 10 (3), 282-290.

Tolson, B.A., Shoemaker, C.A., 2007. Dynamically dimensioned search algorithm for computationally efficient watershed model calibration. Water Resources Research 43 (1), W01413.

U.S. Geological Survey, 2026, USGS Water Data for the Nation, accessed 18 November 2026, at https://doi.org/10.5066/F7P55KJN. The record used is the daily mean discharge (parameter 00060, statistic 00003) at site 01030500, Mattawamkeag River near Mattawamkeag, Maine, from 1 January 1997 to 31 December 2025.

## Video

--8<-- "include/slots/12_calibrate.html"

## Next

- [Calibrate on several gauges and variables](calibrate-several.md) adds more measured series to a calibration.
- [Uncertainty analysis](uncertainty.md) puts a band around the simulated flow.
- [Change inputs](change-inputs.md) shows what else SWATrust lets you set.
