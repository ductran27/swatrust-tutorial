# Uncertainty analysis

This page shows how to put a band of uncertainty around the simulated flow with SUFI-2 or GLUE, and how to read the band.

## What the band is

The Calibration page calls one run of the model with one set of parameter values a simulation. One simulation gives one simulated flow for each day. An uncertainty analysis makes many simulations, each with another set of parameter values, and keeps the simulated flow of each. The band is the range, on each day, between a low and a high value of these simulated flows.

SWATrust offers two methods on the **Calibration** page: SUFI-2 and GLUE. By default, the band of SUFI-2 holds the middle 95 % of the simulated flows of the sets of an iteration, and the band of GLUE holds the middle 95 % of the simulated flows of the sets that it keeps, counted by their weight. The "i" beside **Method** says of SUFI-2 "iterations of sets that give a band for each row and narrower ranges", and of GLUE "many random sets; the sets that fit well enough give limits for each row". A row is one measured series under **Measured data**; in this chapter it is the flow at the gauge.

## What you need

- The model and the measured flow file of [Calibrate and validate](calibrate.md): the basin 01020003, and the daily flow of the gauge 01030500.
- The three periods of that page: the warm-up 2010, the calibration years 2011 to 2012, and the validation years 2013 to 2014. This page keeps the periods short and the number of sets small so that the analysis stays small.

## SUFI-2

SUFI-2 works in iterations.

1. An iteration draws \(n\) sets of parameter values by Latin hypercube sampling: the range of each parameter is cut into \(n\) equal parts, and each part gives one value.
2. The band of the iteration is formed, on each day, by the 2.5 % and the 97.5 % values of the simulated flows of the \(n\) sets of the iteration. Every simulation has the same weight.
3. When it can, the iteration proposes new ranges of the parameters for the next iteration.

The new range of a parameter is

\[
b'_{min} = b_{lower} - \max\!\left(\frac{b_{lower} - b_{min}}{2}, \frac{b_{max} - b_{upper}}{2}\right)
\]

\[
b'_{max} = b_{upper} + \max\!\left(\frac{b_{lower} - b_{min}}{2}, \frac{b_{max} - b_{upper}}{2}\right)
\]

where \(b_{min}\) and \(b_{max}\) are the limits of the range that the iteration sampled, and \(b_{lower}\) and \(b_{upper}\) are the 95 % confidence limits of the parameter around its value in the best simulation of the iteration (Abbaspour et al., 2004, 2007). A new range does not pass the outer limits of the parameter. For a parameter on the log scale, \(b\) is the logarithm of its value, in the sampling and in the new range.

A new range can be wider than the range that was sampled. An iteration does not always narrow a range.

### Set the analysis

1. In **Set-up**, click **Clear choice** and tick the model 01020003, so that it is the only model chosen.
2. Click **Calibration**, the fourth of the four views. The box **Model** names the model.
3. In the bar **Method**, click **SUFI-2**.
4. Under **Measured file**, check that the box holds the path of the measured flow file of [Calibrate and validate](calibrate.md#get-the-measured-flow), and that the line under it counts the file's days. If the box is empty, click **Download**, as [Calibrate and validate](calibrate.md#get-the-measured-flow) shows.
5. Under **Objective function**, leave **KGE daily**.
6. Under **Years**, check the three periods: 2010 to 2010, 2011 to 2012, and 2013 to 2014.
7. In **Simulations per iteration**, type `50` and press ++enter++.

The line above the button now reads "51 simulations: iteration 1, 1 initial + 50 evenly spread sets | 13 parameters". The simulation named "initial" is made with the initial parameters, the values that the model has before the analysis.

--8<-- "include/shots/s13_4_sufi2_setup.html"

| Box | What it sets | As the page opens |
|---|---|---|
| **Objective function** | the statistic that ranks the sets over the calibration years | KGE daily |
| **Years** | the warm-up, the calibration years and the validation years | the periods of the search |
| **Where** | the channel compared with the measured flow | the channel that the page proposes |
| **Simulations per iteration** | the number of sets of one iteration, up to 2,000 | 500 |
| **Behavioral threshold** | the value of the objective function that a simulation must reach | empty |
| **Best simulations used** | the number of best simulations that set the new ranges | 1 |
| **Band levels, %** | the two levels of the band | 2.5 % and 97.5 % |

The page says of **Behavioral threshold**: "Left empty, every simulation that gave a flow series makes the band. With a value, only the simulations whose objective reaches it make the band." Of **Best simulations used** it says: "The new ranges are centered on the best simulation. With more than 1, the widest range among the best simulations is taken for each parameter."

The block **Parameters** lists the parameters with their ranges on the tab **Ranges**. The sets are drawn between **Lowest** and **Highest**. [Calibrate and validate](calibrate.md#choose-the-parameters-and-their-ranges) describes the list.

### Start and read the band

1. Click **Start iteration 1**.

    Under the boxes, a table lists three steps: **Initial simulation**, **Iteration 1** and **Band, new ranges**.

2. Wait until the block **Result** reads "done, 50 sets".

The chart **Daily flow** draws four things: the measured flow, the band named "95PPU", the middle line named "50 %", and the simulated flow of the best simulation. It opens on the years after the warm-up, 2011 to 2014. The shaded years are the calibration years. **Two years** shows two years, and the button then reads **All years**.

The block **Result** gives the table **95PPU**, the table of the band. In the walk of this page it read as follows.

| | Calibration | Validation |
|---|---|---|
| Days | 731 | 730 |
| Measured days | 731 | 730 |
| Inside the band | 529 | 435 |
| p-factor | 0.72 | 0.60 |
| Mean band width, m³/s | 61.6 | 64.1 |
| SD of measured flow, m³/s | 95.7 | 112 |
| r-factor | 0.64 | 0.57 |

The p-factor is the share of the days with a measured flow on which the measured flow lies inside the band. A day on which the measured flow equals a limit of the band counts as inside.

The r-factor is the mean width of the band, divided by the standard deviation of the measured flow:

\[
r = \frac{\bar{d}}{\sigma_O}, \qquad \bar{d} = \frac{1}{k} \sum_{i=1}^{k} \left(q_{U,i} - q_{L,i}\right)
\]

where \(q_{U,i}\) and \(q_{L,i}\) are the upper and the lower limit of the band on day \(i\) (m³/s), \(k\) is the number of days with a measured flow, and \(\sigma_O\) is the standard deviation of the measured flow on those days (m³/s). In the table, \(\bar{d}\) is the row **Mean band width** and \(\sigma_O\) is the row **SD of measured flow**.

A p-factor near 1 means that the band holds nearly all of the measured flows. A small r-factor means a narrow band compared with the spread of the measured flow. A wider band holds at least as many measured flows and has a larger r-factor, so the two factors are read together (Abbaspour et al., 2004, 2007).

--8<-- "include/shots/s13_5_sufi2_band.html"

### The tabs of Parameters

| Tab | What it shows |
|---|---|
| **Ranges** | initial value and sampled range of each parameter |
| **Simulations** | statistics, behavioral or not, and parameter values of each simulation |
| **Statistics** | best simulation and initial parameters, daily and monthly, both periods |
| **Sensitivity** | slope, standard error, t, p and rank of each parameter |
| **New ranges** | the range that the iteration suggests for each parameter |
| **Correlation** | a table of correlations between the parameters |

The tab **Simulations** has one line for each simulation, with NSE, KGE and PBIAS in both periods.

The **Sensitivity** tab fits the value of the objective function in the iteration's simulations (the daily KGE or NSE of the calibration period) as a straight-line function of the parameter values, \(g = \alpha + \sum_j \beta_j b_j\). For each parameter it gives the slope, its standard error, t (the slope over its standard error), the two-sided p-value, and the rank by the size of t, 1 for the most sensitive. For a parameter on the log scale the slope is per tenfold change of its value.

The **Correlation** tab gives, for each pair of parameters, the correlation of their estimates from the iteration, computed from how the objective function changes between every two simulations (Abbaspour et al., 2004, 2007). Pairs at 0.8 or more in size are marked; the page names the less sensitive of each such pair and leaves the choice of fixing it to you.

The tab **New ranges** puts the terms of the two equations side by side. The column **Range sampled** gives \(b_{min}\) and \(b_{max}\), the columns **Interval of the best value** give \(b_{lower}\) and \(b_{upper}\), and the column **Before the cut** gives \(b'_{min}\) and \(b'_{max}\). The columns **Suggested range** give the new range after it was cut at the allowed range.

For the parameter cn2, the walk of this page gave the range sampled as -10 to 10 and the interval of the best value as -4.7206 to -4.62016. The larger of the two halves is

\[
\max\!\left(\frac{-4.7206 - (-10)}{2}, \frac{10 - (-4.62016)}{2}\right) = 7.31008
\]

so the new range runs from \(-4.7206 - 7.31008\), about -12.03, to \(-4.62016 + 7.31008\), about 2.69. The column **Before the cut** shows it as "-12.0307 to 2.68992", and the boxes **Lowest** and **Highest** under **Suggested range** hold -12.0307 and 2.68992. This range reaches below the range that was sampled, and the page says so under the table.

--8<-- "include/shots/s13_6_sufi2_new_ranges.html"

--8<-- "include/shots/s13_6c_under_table.html"

--8<-- "include/shots/s13_6b_before_cut.html"

Under **Notes**, the page lists the note "New ranges: where the best simulations lie". The suggested ranges show mainly where the best simulation lies: they are centered on it and span half to all of the range sampled, so that one iteration can at most halve a range.

## GLUE

GLUE draws many sets of parameter values and gives each set a likelihood measure, which says how well its simulated flow fits the measured flow. The likelihood measure \(M\) is the daily NSE or the daily KGE of the calibration years.

A set is kept when its likelihood measure reaches a behavioral threshold \(T\):

\[
M \ge T
\]

A kept set is called behavioral. SWATrust gives each behavioral set a weight from its likelihood measure:

\[
w_j = \frac{M_j^{\,N}}{\sum_{k} M_k^{\,N}}
\]

where \(w_j\) is the weight of the behavioral set \(j\), \(M_j\) is its likelihood measure, the sum runs over all behavioral sets, and \(N\) is an exponent that the page lets you set under the name **Shaping factor**. \(N\) is 1 unless you change it. A weight as a share of the sum over the kept sets is the form that Beven and Binley (2014) give for sets drawn at random within their ranges. The exponent \(N\) is SWATrust's own form.

On each day, the band runs from the weighted 2.5 % value to the weighted 97.5 % value of the simulated flows of the behavioral sets. The page can use the 5 % and the 95 % values instead. The middle line is the weighted 50 % value.

### Set the analysis

1. In the bar **Method**, click **GLUE**.
2. Under **Likelihood measure**, leave **NSE daily**.
3. Check the three periods under **Years**.
4. In **Simulations**, type `100` and press ++enter++.

The line above the button now reads "101 simulations: 1 initial + 100 random sets | 13 parameters".

--8<-- "include/shots/s13_1_glue_setup.html"

The page also holds **Where**, as for SUFI-2, and these boxes.

| Box | What it sets | As the page opens |
|---|---|---|
| **Simulations** | the number of random sets, from 100 to 2,000 | 1000 |
| **Behavioral threshold** | the behavioral threshold \(T\) | 0.5 |
| **Shaping factor** | the exponent \(N\) | 1 |
| **Prediction limits** | the band's levels: **2.5 % and 97.5 %** or **5 % and 95 %** | 2.5 % and 97.5 % |
| **Time limit per simulation, s** | the longest that one simulation may take, in seconds | a number of the page |

The sets are scored on the calibration years; the validation and the warm-up years take no part.

### Start and watch

1. Click **Start GLUE**.

    Under the boxes, a table lists three steps: **Initial simulation**, **Random sets** and **Prediction limits**. The block **Result** counts the simulations, as in "running, 42 of 101 simulations". The button **Stop** stands where **Start GLUE** stood.

2. Wait until the block **Result** reads "done, 100 sets".

The simulations go on in the launcher while the page is closed. Open the page again, and it shows the state of the analysis.

### Read the band

The chart **Daily flow** draws the same four things, and it names the band "95 % prediction limits".

--8<-- "include/shots/s13_2_glue_band.html"

The block **Result** gives the table of the band, here under the heading **Band**, with the rows that it has for SUFI-2. In the walk of this page it read as follows.

| | Calibration | Validation |
|---|---|---|
| Days | 731 | 730 |
| Measured days | 731 | 730 |
| Inside the band | 314 | 243 |
| p-factor | 0.43 | 0.33 |
| Mean band width, m³/s | 38.3 | 45.6 |
| SD of measured flow, m³/s | 95.7 | 112 |
| r-factor | 0.40 | 0.41 |

This band is narrower than the band of SUFI-2 above, and it holds fewer of the measured flows. The two bands are not made from the same sets: SUFI-2 takes every set of the iteration, and GLUE takes the behavioral sets only.

The "i" beside the heading **Band** says how the band was made. In the walk of this page, 13 of the 100 sets were behavioral, with an NSE of at least 0.5 in the calibration years, and on each day the prediction limits held 95 % of the likelihood-weighted flows of these sets. The first paragraph of the "i" ends: "They are not a promise about future measured flows."

Thirteen behavioral sets are few. Click **Notes** under the table to see what the page says of the result. In the walk of this page the first note was "Few behavioral simulations: 13". Prediction limits that rest on fewer than 30 behavioral simulations can change much when more simulations are added.

--8<-- "include/shots/s13_3_glue_factors.html"

### Move the threshold

The box **Behavioral threshold** under the table moves the threshold \(T\) after the simulations. The page says of it: "Moving the threshold redraws the prediction limits at once; no new simulations are needed."

1. In **Behavioral threshold**, type `0.4` and press ++enter++.

    The band is drawn again from the same 100 simulations. In the walk of this page the table changed as follows.

    | | Calibration | Validation |
    |---|---|---|
    | Inside the band | 429 | 328 |
    | p-factor | 0.59 | 0.45 |
    | Mean band width, m³/s | 46.4 | 53.6 |
    | r-factor | 0.49 | 0.48 |

2. Type `0.5` and press ++enter++ to go back.

In this walk, the band at 0.4 is wider than the band at 0.5, and it holds more of the measured flows. A threshold that no simulation reaches leaves no band, and the page says so. With `0.9`, the page named the NSE that the best simulation reached and advised to lower the threshold or to widen the ranges.

### The tabs of Parameters

| Tab | What it shows |
|---|---|
| **Ranges** | initial value, sampled range and allowed range of each parameter |
| **Simulations** | statistics, behavioral or not, likelihood, weight and parameter values of each simulation |
| **Statistics** | best simulation and initial parameters, daily and monthly, both periods |
| **Parameter values** | weighted 2.5 %, 50 % and 97.5 % values, lowest, highest and best |

The tab **Simulations** has one line for each simulation, with NSE, KGE and PBIAS in the calibration and in the validation years. The tab **Parameter values** gives, beside the weighted values, the lowest and the highest value among the behavioral simulations and the value of the best simulation.

The page says of the button **CSV** beside the heading **Parameters**: "Save the table in view as a CSV file".

## The folder of an analysis

Each analysis has a folder of its own in the runs folder, named `uq_<date>_<time>`.

```text
~/SWATrust/runs/
    uq_<date>_<time>/
        uq.json
        runs.tsv
        dates.tsv
        obs.txt
        model_key.tsv
        calibration_base.cal
        gauges/
        series/
        slots/
```

The file `runs.tsv` has a line of names and then one line for each simulation. The folder `series/` has one file for each simulation, and the folder `slots/` holds the copies of the model that the simulations were made on. The analysis writes nothing into the folder of the model.

## What the band does not say

The band is made only from the simulations that were made: parameter values drawn inside the ranges set on the page. No error of the measured flow or of the weather is added to it.

For GLUE, the band depends on the likelihood measure, the behavioral threshold and the exponent \(N\) that were chosen. Moving the threshold redraws it at once, from the same simulations.

The page says of the prediction limits of GLUE: "They are not a promise about future measured flows." Of both methods it says: "The result is the band and the ranges, not one set."

## References

Abbaspour, K.C., Johnson, C.A., van Genuchten, M.Th., 2004. Estimating uncertain flow and transport parameters using a sequential uncertainty fitting procedure. Vadose Zone Journal 3, 1340-1352.

Abbaspour, K.C., Yang, J., Maximov, I., Siber, R., Bogner, K., Mieleitner, J., Zobrist, J., Srinivasan, R., 2007. Modelling hydrology and water quality in the pre-alpine/alpine Thur watershed using SWAT. Journal of Hydrology 333, 413-430.

Beven, K., Binley, A., 2014. GLUE: 20 years on. Hydrological Processes 28, 5897-5918.

## Video

--8<-- "include/slots/13_uncertainty.html"

## Next

- [Change inputs](change-inputs.md) shows what else SWATrust lets you set.
- [Glossary](glossary.md) explains the terms of this page.
