Toggle navigationTitanic Profiling Report

  * Overview
  * Variables
  * Interactions
  * Correlations
  * Missing values
  * Sample

# Overview

Brought to you by
[YData](https://ydata.ai/?utm_source=opensource&utm_medium=ydataprofiling&utm_campaign=report)

  * Overview
  * Alerts 6
  * Reproduction

Dataset statistics

Number of variables| 8  
---|---  
Number of observations| 887  
Missing cells| 0  
Missing cells (%)| 0.0%  
Duplicate rows| 0  
Duplicate rows (%)| 0.0%  
Total size in memory| 166.5 KiB  
Average record size in memory| 192.2 B  
  
Variable types

Categorical| 3  
---|---  
Text| 1  
Numeric| 4  
  
Alerts

`Sex` is highly overall correlated with `Survived`| High correlation  
---|---  
`Survived` is highly overall correlated with `Sex`| High correlation  
`Name` has unique values| Unique  
`Siblings/Spouses Aboard` has 604 (68.1%) zeros| Zeros  
`Parents/Children Aboard` has 674 (76.0%) zeros| Zeros  
`Fare` has 15 (1.7%) zeros| Zeros  
  
Reproduction

Analysis started| 2024-09-13 22:50:32.377914  
---|---  
Analysis finished| 2024-09-13 22:50:38.290607  
Duration| 5.91 seconds  
Software version| [ydata-profiling vv4.10.0](https://github.com/ydataai/ydata-
profiling)  
Download configuration|
[config.json](data:text/plain;charset=utf-8,%7B%22title%22%3A%20%22Titanic%20Profiling%20Report%22%2C%20%22dataset%22%3A%20%7B%22description%22%3A%20%22%22%2C%20%22creator%22%3A%20%22%22%2C%20%22author%22%3A%20%22%22%2C%20%22copyright_holder%22%3A%20%22%22%2C%20%22copyright_year%22%3A%20%22%22%2C%20%22url%22%3A%20%22%22%7D%2C%20%22variables%22%3A%20%7B%22descriptions%22%3A%20%7B%7D%7D%2C%20%22infer_dtypes%22%3A%20true%2C%20%22show_variable_description%22%3A%20true%2C%20%22pool_size%22%3A%200%2C%20%22progress_bar%22%3A%20true%2C%20%22vars%22%3A%20%7B%22num%22%3A%20%7B%22quantiles%22%3A%20%5B0.05%2C%200.25%2C%200.5%2C%200.75%2C%200.95%5D%2C%20%22skewness_threshold%22%3A%2020%2C%20%22low_categorical_threshold%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%7D%2C%20%22text%22%3A%20%7B%22length%22%3A%20true%2C%20%22words%22%3A%20true%2C%20%22characters%22%3A%20true%2C%20%22redact%22%3A%20false%7D%2C%20%22cat%22%3A%20%7B%22length%22%3A%20true%2C%20%22characters%22%3A%20true%2C%20%22words%22%3A%20true%2C%20%22cardinality_threshold%22%3A%2050%2C%20%22percentage_cat_threshold%22%3A%200.5%2C%20%22imbalance_threshold%22%3A%200.5%2C%20%22n_obs%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%2C%20%22coerce_str_to_date%22%3A%20false%2C%20%22redact%22%3A%20false%2C%20%22histogram_largest%22%3A%2050%2C%20%22stop_words%22%3A%20%5B%5D%7D%2C%20%22image%22%3A%20%7B%22active%22%3A%20true%2C%20%22exif%22%3A%20true%2C%20%22hash%22%3A%20true%7D%2C%20%22bool%22%3A%20%7B%22n_obs%22%3A%203%2C%20%22imbalance_threshold%22%3A%200.5%2C%20%22mappings%22%3A%20%7B%22t%22%3A%20true%2C%20%22f%22%3A%20false%2C%20%22yes%22%3A%20true%2C%20%22no%22%3A%20false%2C%20%22y%22%3A%20true%2C%20%22n%22%3A%20false%2C%20%22true%22%3A%20true%2C%20%22false%22%3A%20false%7D%7D%2C%20%22path%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22file%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22url%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22timeseries%22%3A%20%7B%22active%22%3A%20false%2C%20%22sortby%22%3A%20null%2C%20%22autocorrelation%22%3A%200.7%2C%20%22lags%22%3A%20%5B1%2C%207%2C%2012%2C%2024%2C%2030%5D%2C%20%22significance%22%3A%200.05%2C%20%22pacf_acf_lag%22%3A%20100%7D%7D%2C%20%22sort%22%3A%20null%2C%20%22missing_diagrams%22%3A%20%7B%22bar%22%3A%20true%2C%20%22matrix%22%3A%20true%2C%20%22heatmap%22%3A%20true%7D%2C%20%22correlation_table%22%3A%20true%2C%20%22correlations%22%3A%20%7B%22auto%22%3A%20%7B%22key%22%3A%20%22auto%22%2C%20%22calculate%22%3A%20true%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22spearman%22%3A%20%7B%22key%22%3A%20%22spearman%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22pearson%22%3A%20%7B%22key%22%3A%20%22pearson%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22phi_k%22%3A%20%7B%22key%22%3A%20%22phi_k%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22cramers%22%3A%20%7B%22key%22%3A%20%22cramers%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22kendall%22%3A%20%7B%22key%22%3A%20%22kendall%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%7D%2C%20%22interactions%22%3A%20%7B%22continuous%22%3A%20true%2C%20%22targets%22%3A%20%5B%5D%7D%2C%20%22categorical_maximum_correlation_distinct%22%3A%20100%2C%20%22memory_deep%22%3A%20true%2C%20%22plot%22%3A%20%7B%22missing%22%3A%20%7B%22force_labels%22%3A%20true%2C%20%22cmap%22%3A%20%22RdBu%22%7D%2C%20%22image_format%22%3A%20%22svg%22%2C%20%22correlation%22%3A%20%7B%22cmap%22%3A%20%22RdBu%22%2C%20%22bad%22%3A%20%22%23000000%22%7D%2C%20%22dpi%22%3A%20800%2C%20%22histogram%22%3A%20%7B%22bins%22%3A%2050%2C%20%22max_bins%22%3A%20250%2C%20%22x_axis_labels%22%3A%20true%2C%20%22density%22%3A%20false%7D%2C%20%22scatter_threshold%22%3A%201000%2C%20%22cat_freq%22%3A%20%7B%22show%22%3A%20true%2C%20%22type%22%3A%20%22bar%22%2C%20%22max_unique%22%3A%2010%2C%20%22colors%22%3A%20null%7D%2C%20%22font_path%22%3A%20null%7D%2C%20%22duplicates%22%3A%20%7B%22head%22%3A%2010%2C%20%22key%22%3A%20%22%23%20duplicates%22%7D%2C%20%22samples%22%3A%20%7B%22head%22%3A%2010%2C%20%22tail%22%3A%2010%2C%20%22random%22%3A%200%7D%2C%20%22reject_variables%22%3A%20true%2C%20%22n_obs_unique%22%3A%2010%2C%20%22n_freq_table_max%22%3A%2010%2C%20%22n_extreme_obs%22%3A%2010%2C%20%22report%22%3A%20%7B%22precision%22%3A%208%7D%2C%20%22html%22%3A%20%7B%22style%22%3A%20%7B%22primary_colors%22%3A%20%5B%22%23377eb8%22%2C%20%22%23e41a1c%22%2C%20%22%234daf4a%22%5D%2C%20%22logo%22%3A%20%22%22%2C%20%22theme%22%3A%20null%7D%2C%20%22navbar_show%22%3A%20true%2C%20%22minify_html%22%3A%20true%2C%20%22use_local_assets%22%3A%20true%2C%20%22inline%22%3A%20true%2C%20%22assets_prefix%22%3A%20null%2C%20%22assets_path%22%3A%20null%2C%20%22full_width%22%3A%20false%7D%2C%20%22notebook%22%3A%20%7B%22iframe%22%3A%20%7B%22height%22%3A%20%22800px%22%2C%20%22width%22%3A%20%22100%25%22%2C%20%22attribute%22%3A%20%22srcdoc%22%7D%7D%7D)  
  
# Variables

Select ColumnsSurvivedPclassNameSexAgeSiblings/Spouses AboardParents/Children
AboardFare

Survived  
Categorical

`HIGH CORRELATION`

Distinct| 2  
---|---  
Distinct (%)| 0.2%  
Missing| 0  
Missing (%)| 0.0%  
Memory size| 50.4 KiB  
  
0 |  545   
---|---  
1 |  342   
  
More details

  * Overview
  * Categories
  * Words
  * Characters

Length

Max length| 1  
---|---  
Median length| 1  
Mean length| 1  
Min length| 1  
  
Characters and Unicode

Total characters| 887  
---|---  
Distinct characters| 2  
Distinct categories| 1
[?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category
"Unicode categories \(click for more information\)")  
Distinct scripts| 1
[?](https://en.wikipedia.org/wiki/Script_\(Unicode\)#List_of_scripts_in_Unicode
"Unicode scripts \(click for more information\)")  
Distinct blocks| 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode
blocks \(click for more information\)")  
  
The Unicode Standard assigns character properties to each code point, which
can be used to analyse textual variables.

Unique

Unique| 0 ?  
---|---  
Unique (%)| 0.0%  
  
Sample

1st row| 0  
---|---  
2nd row| 1  
3rd row| 1  
4th row| 1  
5th row| 0  
  
#### Common Values

Value| Count| Frequency (%)  
---|---|---  
0 | 545|  61.4%   
1 | 342|  38.6%   
  
#### Length

2024-09-13T22:50:38.349576image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

Histogram of lengths of the category

#### Common Values (Plot)

2024-09-13T22:50:38.444820image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

Value| Count| Frequency (%)  
---|---|---  
0 | 545|  61.4%   
1 | 342|  38.6%   
  
  * Characters
  * Categories
  * Scripts
  * Blocks

#### Most occurring characters

Value| Count| Frequency (%)  
---|---|---  
0 | 545|  61.4%   
1 | 342|  38.6%   
  
#### Most occurring categories

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 887|  100.0%   
  
#### Most frequent character per category

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
0 | 545|  61.4%   
1 | 342|  38.6%   
  
#### Most occurring scripts

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 887|  100.0%   
  
#### Most frequent character per script

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
0 | 545|  61.4%   
1 | 342|  38.6%   
  
#### Most occurring blocks

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 887|  100.0%   
  
#### Most frequent character per block

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
0 | 545|  61.4%   
1 | 342|  38.6%   
  
Pclass  
Categorical

Distinct| 3  
---|---  
Distinct (%)| 0.3%  
Missing| 0  
Missing (%)| 0.0%  
Memory size| 50.4 KiB  
  
3 |  487   
---|---  
1 |  216   
2 |  184   
  
More details

  * Overview
  * Categories
  * Words
  * Characters

Length

Max length| 1  
---|---  
Median length| 1  
Mean length| 1  
Min length| 1  
  
Characters and Unicode

Total characters| 887  
---|---  
Distinct characters| 3  
Distinct categories| 1
[?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category
"Unicode categories \(click for more information\)")  
Distinct scripts| 1
[?](https://en.wikipedia.org/wiki/Script_\(Unicode\)#List_of_scripts_in_Unicode
"Unicode scripts \(click for more information\)")  
Distinct blocks| 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode
blocks \(click for more information\)")  
  
The Unicode Standard assigns character properties to each code point, which
can be used to analyse textual variables.

Unique

Unique| 0 ?  
---|---  
Unique (%)| 0.0%  
  
Sample

1st row| 3  
---|---  
2nd row| 1  
3rd row| 3  
4th row| 1  
5th row| 3  
  
#### Common Values

Value| Count| Frequency (%)  
---|---|---  
3 | 487|  54.9%   
1 | 216|  24.4%   
2 | 184|    20.7%   
  
#### Length

2024-09-13T22:50:38.542068image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

Histogram of lengths of the category

#### Common Values (Plot)

2024-09-13T22:50:38.639776image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

Value| Count| Frequency (%)  
---|---|---  
3 | 487|  54.9%   
1 | 216|  24.4%   
2 | 184|    20.7%   
  
  * Characters
  * Categories
  * Scripts
  * Blocks

#### Most occurring characters

Value| Count| Frequency (%)  
---|---|---  
3 | 487|  54.9%   
1 | 216|  24.4%   
2 | 184|    20.7%   
  
#### Most occurring categories

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 887|  100.0%   
  
#### Most frequent character per category

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
3 | 487|  54.9%   
1 | 216|  24.4%   
2 | 184|    20.7%   
  
#### Most occurring scripts

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 887|  100.0%   
  
#### Most frequent character per script

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
3 | 487|  54.9%   
1 | 216|  24.4%   
2 | 184|    20.7%   
  
#### Most occurring blocks

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 887|  100.0%   
  
#### Most frequent character per block

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
3 | 487|  54.9%   
1 | 216|  24.4%   
2 | 184|    20.7%   
  
Name  
Text

`UNIQUE`

Distinct| 887  
---|---  
Distinct (%)| 100.0%  
Missing| 0  
Missing (%)| 0.0%  
Memory size| 71.4 KiB  
  
2024-09-13T22:50:38.873014image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

More details

  * Overview
  * Words
  * Characters

Length

Max length| 81  
---|---  
Median length| 50  
Mean length| 25.322435  
Min length| 11  
  
Characters and Unicode

Total characters| 22461  
---|---  
Distinct characters| 58  
Distinct categories| 1
[?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category
"Unicode categories \(click for more information\)")  
Distinct scripts| 1
[?](https://en.wikipedia.org/wiki/Script_\(Unicode\)#List_of_scripts_in_Unicode
"Unicode scripts \(click for more information\)")  
Distinct blocks| 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode
blocks \(click for more information\)")  
  
The Unicode Standard assigns character properties to each code point, which
can be used to analyse textual variables.

Unique

Unique| 887 ?  
---|---  
Unique (%)| 100.0%  
  
Sample

1st row| Mr. Owen Harris Braund  
---|---  
2nd row| Mrs. John Bradley (Florence Briggs Thayer) Cumings  
3rd row| Miss. Laina Heikkinen  
4th row| Mrs. Jacques Heath (Lily May Peel) Futrelle  
5th row| Mr. William Henry Allen  
  
Value| Count| Frequency (%)  
---|---|---  
mr | 513|    14.5%   
miss | 182|    5.1%   
mrs | 125|    3.5%   
william | 62|    1.8%   
john | 44|    1.2%   
master | 40|    1.1%   
henry | 33|    0.9%   
james | 24|    0.7%   
charles | 23|    0.7%   
george | 22|    0.6%   
Other values (1482) | 2468|  69.8%   
  
2024-09-13T22:50:39.279019image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

  * Characters
  * Categories
  * Scripts
  * Blocks

#### Most occurring characters

Value| Count| Frequency (%)  
---|---|---  
| 2649|    11.8%  
r | 1914|    8.5%   
e | 1654|    7.4%   
a | 1618|    7.2%   
i | 1287|    5.7%   
s | 1281|    5.7%   
n | 1273|    5.7%   
M | 1105|    4.9%   
l | 1039|    4.6%   
o | 986|    4.4%   
Other values (48) | 7655|  34.1%   
  
#### Most occurring categories

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 22461|  100.0%   
  
#### Most frequent character per category

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
| 2649|    11.8%  
r | 1914|    8.5%   
e | 1654|    7.4%   
a | 1618|    7.2%   
i | 1287|    5.7%   
s | 1281|    5.7%   
n | 1273|    5.7%   
M | 1105|    4.9%   
l | 1039|    4.6%   
o | 986|    4.4%   
Other values (48) | 7655|  34.1%   
  
#### Most occurring scripts

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 22461|  100.0%   
  
#### Most frequent character per script

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
| 2649|    11.8%  
r | 1914|    8.5%   
e | 1654|    7.4%   
a | 1618|    7.2%   
i | 1287|    5.7%   
s | 1281|    5.7%   
n | 1273|    5.7%   
M | 1105|    4.9%   
l | 1039|    4.6%   
o | 986|    4.4%   
Other values (48) | 7655|  34.1%   
  
#### Most occurring blocks

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 22461|  100.0%   
  
#### Most frequent character per block

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
| 2649|    11.8%  
r | 1914|    8.5%   
e | 1654|    7.4%   
a | 1618|    7.2%   
i | 1287|    5.7%   
s | 1281|    5.7%   
n | 1273|    5.7%   
M | 1105|    4.9%   
l | 1039|    4.6%   
o | 986|    4.4%   
Other values (48) | 7655|  34.1%   
  
Sex  
Categorical

`HIGH CORRELATION`

Distinct| 2  
---|---  
Distinct (%)| 0.2%  
Missing| 0  
Missing (%)| 0.0%  
Memory size| 53.6 KiB  
  
male |  573   
---|---  
female |  314   
  
More details

  * Overview
  * Categories
  * Words
  * Characters

Length

Max length| 6  
---|---  
Median length| 4  
Mean length| 4.7080045  
Min length| 4  
  
Characters and Unicode

Total characters| 4176  
---|---  
Distinct characters| 5  
Distinct categories| 1
[?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category
"Unicode categories \(click for more information\)")  
Distinct scripts| 1
[?](https://en.wikipedia.org/wiki/Script_\(Unicode\)#List_of_scripts_in_Unicode
"Unicode scripts \(click for more information\)")  
Distinct blocks| 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode
blocks \(click for more information\)")  
  
The Unicode Standard assigns character properties to each code point, which
can be used to analyse textual variables.

Unique

Unique| 0 ?  
---|---  
Unique (%)| 0.0%  
  
Sample

1st row| male  
---|---  
2nd row| female  
3rd row| female  
4th row| female  
5th row| male  
  
#### Common Values

Value| Count| Frequency (%)  
---|---|---  
male | 573|  64.6%   
female | 314|  35.4%   
  
#### Length

2024-09-13T22:50:39.415333image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

Histogram of lengths of the category

#### Common Values (Plot)

2024-09-13T22:50:39.521356image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

Value| Count| Frequency (%)  
---|---|---  
male | 573|  64.6%   
female | 314|  35.4%   
  
  * Characters
  * Categories
  * Scripts
  * Blocks

#### Most occurring characters

Value| Count| Frequency (%)  
---|---|---  
e | 1201|  28.8%   
m | 887|  21.2%   
a | 887|  21.2%   
l | 887|  21.2%   
f | 314|    7.5%   
  
#### Most occurring categories

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 4176|  100.0%   
  
#### Most frequent character per category

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
e | 1201|  28.8%   
m | 887|  21.2%   
a | 887|  21.2%   
l | 887|  21.2%   
f | 314|    7.5%   
  
#### Most occurring scripts

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 4176|  100.0%   
  
#### Most frequent character per script

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
e | 1201|  28.8%   
m | 887|  21.2%   
a | 887|  21.2%   
l | 887|  21.2%   
f | 314|    7.5%   
  
#### Most occurring blocks

Value| Count| Frequency (%)  
---|---|---  
(unknown) | 4176|  100.0%   
  
#### Most frequent character per block

#####  _(unknown)_

Value| Count| Frequency (%)  
---|---|---  
e | 1201|  28.8%   
m | 887|  21.2%   
a | 887|  21.2%   
l | 887|  21.2%   
f | 314|    7.5%   
  
Age  
Real number (ℝ)

Distinct| 89  
---|---  
Distinct (%)| 10.0%  
Missing| 0  
Missing (%)| 0.0%  
Infinite| 0  
Infinite (%)| 0.0%  
Mean| 29.471443  
  
Minimum| 0.42  
---|---  
Maximum| 80  
Zeros| 0  
Zeros (%)| 0.0%  
Negative| 0  
Negative (%)| 0.0%  
Memory size| 7.1 KiB  
  
2024-09-13T22:50:39.634088image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

More details

  * Statistics
  * Histogram
  * Common values
  * Extreme values

Quantile statistics

Minimum| 0.42  
---|---  
5-th percentile| 5  
Q1| 20.25  
median| 28  
Q3| 38  
95-th percentile| 55.85  
Maximum| 80  
Range| 79.58  
Interquartile range (IQR)| 17.75  
  
Descriptive statistics

Standard deviation| 14.121908  
---|---  
Coefficient of variation (CV)| 0.47917261  
Kurtosis| 0.29255909  
Mean| 29.471443  
Median Absolute Deviation (MAD)| 8  
Skewness| 0.44718857  
Sum| 26141.17  
Variance| 199.4283  
Monotonicity| Not monotonic  
  
2024-09-13T22:50:39.780302image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value| Count| Frequency (%)  
---|---|---  
22 | 39|    4.4%   
28 | 37|    4.2%   
18 | 36|    4.1%   
24 | 34|    3.8%   
21 | 34|    3.8%   
30 | 33|    3.7%   
19 | 33|    3.7%   
27 | 26|    2.9%   
23 | 25|    2.8%   
29 | 25|    2.8%   
Other values (79) | 565|  63.7%   
  
  * Minimum 10 values
  * Maximum 10 values

Value| Count| Frequency (%)  
---|---|---  
0.42 | 1|    0.1%   
0.67 | 1|    0.1%   
0.75 | 2|    0.2%   
0.83 | 2|    0.2%   
0.92 | 1|    0.1%   
1 | 7|  0.8%   
2 | 11|  1.2%   
3 | 7|  0.8%   
4 | 11|  1.2%   
5 | 6|  0.7%   
  
Value| Count| Frequency (%)  
---|---|---  
80 | 1|    0.1%   
74 | 1|    0.1%   
71 | 2|  0.2%   
70.5 | 1|    0.1%   
70 | 2|  0.2%   
69 | 1|    0.1%   
66 | 2|  0.2%   
65 | 3|  0.3%   
64 | 3|  0.3%   
63 | 2|  0.2%   
  
Siblings/Spouses Aboard  
Real number (ℝ)

`ZEROS`

Distinct| 7  
---|---  
Distinct (%)| 0.8%  
Missing| 0  
Missing (%)| 0.0%  
Infinite| 0  
Infinite (%)| 0.0%  
Mean| 0.5253664  
  
Minimum| 0  
---|---  
Maximum| 8  
Zeros| 604  
Zeros (%)| 68.1%  
Negative| 0  
Negative (%)| 0.0%  
Memory size| 7.1 KiB  
  
2024-09-13T22:50:39.902112image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

More details

  * Statistics
  * Histogram
  * Common values
  * Extreme values

Quantile statistics

Minimum| 0  
---|---  
5-th percentile| 0  
Q1| 0  
median| 0  
Q3| 1  
95-th percentile| 3  
Maximum| 8  
Range| 8  
Interquartile range (IQR)| 1  
  
Descriptive statistics

Standard deviation| 1.1046686  
---|---  
Coefficient of variation (CV)| 2.1026631  
Kurtosis| 17.797537  
Mean| 0.5253664  
Median Absolute Deviation (MAD)| 0  
Skewness| 3.6867598  
Sum| 466  
Variance| 1.2202926  
Monotonicity| Not monotonic  
  
2024-09-13T22:50:40.004021image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=7)

Value| Count| Frequency (%)  
---|---|---  
0 | 604|  68.1%   
1 | 209|    23.6%   
2 | 28|    3.2%   
4 | 18|    2.0%   
3 | 16|    1.8%   
8 | 7|    0.8%   
5 | 5|    0.6%   
  
  * Minimum 10 values
  * Maximum 10 values

Value| Count| Frequency (%)  
---|---|---  
0 | 604|  68.1%   
1 | 209|    23.6%   
2 | 28|    3.2%   
3 | 16|    1.8%   
4 | 18|    2.0%   
5 | 5|    0.6%   
8 | 7|    0.8%   
  
Value| Count| Frequency (%)  
---|---|---  
8 | 7|    0.8%   
5 | 5|    0.6%   
4 | 18|    2.0%   
3 | 16|    1.8%   
2 | 28|    3.2%   
1 | 209|    23.6%   
0 | 604|  68.1%   
  
Parents/Children Aboard  
Real number (ℝ)

`ZEROS`

Distinct| 7  
---|---  
Distinct (%)| 0.8%  
Missing| 0  
Missing (%)| 0.0%  
Infinite| 0  
Infinite (%)| 0.0%  
Mean| 0.38331454  
  
Minimum| 0  
---|---  
Maximum| 6  
Zeros| 674  
Zeros (%)| 76.0%  
Negative| 0  
Negative (%)| 0.0%  
Memory size| 7.1 KiB  
  
2024-09-13T22:50:40.101608image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

More details

  * Statistics
  * Histogram
  * Common values
  * Extreme values

Quantile statistics

Minimum| 0  
---|---  
5-th percentile| 0  
Q1| 0  
median| 0  
Q3| 0  
95-th percentile| 2  
Maximum| 6  
Range| 6  
Interquartile range (IQR)| 0  
  
Descriptive statistics

Standard deviation| 0.80746591  
---|---  
Coefficient of variation (CV)| 2.1065361  
Kurtosis| 9.7230659  
Mean| 0.38331454  
Median Absolute Deviation (MAD)| 0  
Skewness| 2.7411981  
Sum| 340  
Variance| 0.65200119  
Monotonicity| Not monotonic  
  
2024-09-13T22:50:40.202584image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=7)

Value| Count| Frequency (%)  
---|---|---  
0 | 674|  76.0%   
1 | 118|    13.3%   
2 | 80|    9.0%   
5 | 5|    0.6%   
3 | 5|    0.6%   
4 | 4|    0.5%   
6 | 1|    0.1%   
  
  * Minimum 10 values
  * Maximum 10 values

Value| Count| Frequency (%)  
---|---|---  
0 | 674|  76.0%   
1 | 118|    13.3%   
2 | 80|    9.0%   
3 | 5|    0.6%   
4 | 4|    0.5%   
5 | 5|    0.6%   
6 | 1|    0.1%   
  
Value| Count| Frequency (%)  
---|---|---  
6 | 1|    0.1%   
5 | 5|    0.6%   
4 | 4|    0.5%   
3 | 5|    0.6%   
2 | 80|    9.0%   
1 | 118|    13.3%   
0 | 674|  76.0%   
  
Fare  
Real number (ℝ)

`ZEROS`

Distinct| 248  
---|---  
Distinct (%)| 28.0%  
Missing| 0  
Missing (%)| 0.0%  
Infinite| 0  
Infinite (%)| 0.0%  
Mean| 32.30542  
  
Minimum| 0  
---|---  
Maximum| 512.3292  
Zeros| 15  
Zeros (%)| 1.7%  
Negative| 0  
Negative (%)| 0.0%  
Memory size| 7.1 KiB  
  
2024-09-13T22:50:40.440108image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

More details

  * Statistics
  * Histogram
  * Common values
  * Extreme values

Quantile statistics

Minimum| 0  
---|---  
5-th percentile| 7.225  
Q1| 7.925  
median| 14.4542  
Q3| 31.1375  
95-th percentile| 112.55749  
Maximum| 512.3292  
Range| 512.3292  
Interquartile range (IQR)| 23.2125  
  
Descriptive statistics

Standard deviation| 49.78204  
---|---  
Coefficient of variation (CV)| 1.5409811  
Kurtosis| 33.264605  
Mean| 32.30542  
Median Absolute Deviation (MAD)| 6.9584  
Skewness| 4.7776714  
Sum| 28654.908  
Variance| 2478.2515  
Monotonicity| Not monotonic  
  
2024-09-13T22:50:40.576731image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

**Histogram with fixed size bins** (bins=50)

Value| Count| Frequency (%)  
---|---|---  
8.05 | 43|    4.8%   
13 | 42|    4.7%   
7.8958 | 36|    4.1%   
7.75 | 33|    3.7%   
26 | 31|    3.5%   
10.5 | 24|    2.7%   
7.925 | 18|    2.0%   
7.775 | 16|    1.8%   
7.2292 | 15|    1.7%   
26.55 | 15|    1.7%   
Other values (238) | 614|  69.2%   
  
  * Minimum 10 values
  * Maximum 10 values

Value| Count| Frequency (%)  
---|---|---  
0 | 15|  1.7%   
4.0125 | 1|    0.1%   
5 | 1|    0.1%   
6.2375 | 1|    0.1%   
6.4375 | 1|    0.1%   
6.45 | 1|    0.1%   
6.4958 | 2|    0.2%   
6.75 | 2|    0.2%   
6.8583 | 1|    0.1%   
6.95 | 1|    0.1%   
  
Value| Count| Frequency (%)  
---|---|---  
512.3292 | 3|  0.3%   
263 | 4|  0.5%   
262.375 | 2|  0.2%   
247.5208 | 2|  0.2%   
227.525 | 4|  0.5%   
221.7792 | 1|    0.1%   
211.5 | 1|    0.1%   
211.3375 | 3|  0.3%   
164.8667 | 2|  0.2%   
153.4625 | 3|  0.3%   
  
# Interactions

  * Age
  * Siblings/Spouses Aboard
  * Parents/Children Aboard
  * Fare

  * Fare
  * Age
  * Siblings/Spouses Aboard
  * Parents/Children Aboard

2024-09-13T22:50:37.701994image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:32.522801image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:32.931536image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:37.161438image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

  * Fare
  * Age
  * Siblings/Spouses Aboard
  * Parents/Children Aboard

2024-09-13T22:50:37.801069image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:32.617179image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:33.003902image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:37.417113image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

  * Fare
  * Age
  * Siblings/Spouses Aboard
  * Parents/Children Aboard

2024-09-13T22:50:37.899572image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:32.729201image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:36.958016image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:37.517400image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

  * Fare
  * Age
  * Siblings/Spouses Aboard
  * Parents/Children Aboard

2024-09-13T22:50:37.991372image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:32.836439image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:37.057988image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

2024-09-13T22:50:37.611527image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

# Correlations

  * Auto

  * Heatmap
  * Table

2024-09-13T22:50:40.662148image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

| Age| Fare| Parents/Children Aboard| Pclass| Sex| Siblings/Spouses Aboard|
Survived  
---|---|---|---|---|---|---|---  
Age| 1.000| 0.156| -0.254| 0.289| 0.119| -0.199| 0.141  
Fare| 0.156| 1.000| 0.409| 0.479| 0.187| 0.446| 0.282  
Parents/Children Aboard| -0.254| 0.409| 1.000| 0.020| 0.246| 0.449| 0.155  
Pclass| 0.289| 0.479| 0.020| 1.000| 0.127| 0.147| 0.335  
Sex| 0.119| 0.187| 0.246| 0.127| 1.000| 0.204| 0.539  
Siblings/Spouses Aboard| -0.199| 0.446| 0.449| 0.147| 0.204| 1.000| 0.186  
Survived| 0.141| 0.282| 0.155| 0.335| 0.539| 0.186| 1.000  
  
# Missing values

  * Count
  * Matrix

2024-09-13T22:50:38.108308image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

A simple visualization of nullity by column.

2024-09-13T22:50:38.239845image/svg+xmlMatplotlib v3.9.2,
https://matplotlib.org/

Nullity matrix is a data-dense display which lets you quickly visually pick
out patterns in data completion.

# Sample

  * First rows
  * Last rows

| Survived| Pclass| Name| Sex| Age| Siblings/Spouses Aboard| Parents/Children
Aboard| Fare  
---|---|---|---|---|---|---|---|---  
0| 0| 3| Mr. Owen Harris Braund| male| 22.0| 1| 0| 7.2500  
1| 1| 1| Mrs. John Bradley (Florence Briggs Thayer) Cumings| female| 38.0| 1|
0| 71.2833  
2| 1| 3| Miss. Laina Heikkinen| female| 26.0| 0| 0| 7.9250  
3| 1| 1| Mrs. Jacques Heath (Lily May Peel) Futrelle| female| 35.0| 1| 0|
53.1000  
4| 0| 3| Mr. William Henry Allen| male| 35.0| 0| 0| 8.0500  
5| 0| 3| Mr. James Moran| male| 27.0| 0| 0| 8.4583  
6| 0| 1| Mr. Timothy J McCarthy| male| 54.0| 0| 0| 51.8625  
7| 0| 3| Master. Gosta Leonard Palsson| male| 2.0| 3| 1| 21.0750  
8| 1| 3| Mrs. Oscar W (Elisabeth Vilhelmina Berg) Johnson| female| 27.0| 0| 2|
11.1333  
9| 1| 2| Mrs. Nicholas (Adele Achem) Nasser| female| 14.0| 1| 0| 30.0708  
  
| Survived| Pclass| Name| Sex| Age| Siblings/Spouses Aboard| Parents/Children
Aboard| Fare  
---|---|---|---|---|---|---|---|---  
877| 0| 3| Mr. Johann Markun| male| 33.0| 0| 0| 7.8958  
878| 0| 3| Miss. Gerda Ulrika Dahlberg| female| 22.0| 0| 0| 10.5167  
879| 0| 2| Mr. Frederick James Banfield| male| 28.0| 0| 0| 10.5000  
880| 0| 3| Mr. Henry Jr Sutehall| male| 25.0| 0| 0| 7.0500  
881| 0| 3| Mrs. William (Margaret Norton) Rice| female| 39.0| 0| 5| 29.1250  
882| 0| 2| Rev. Juozas Montvila| male| 27.0| 0| 0| 13.0000  
883| 1| 1| Miss. Margaret Edith Graham| female| 19.0| 0| 0| 30.0000  
884| 0| 3| Miss. Catherine Helen Johnston| female| 7.0| 1| 2| 23.4500  
885| 1| 1| Mr. Karl Howell Behr| male| 26.0| 0| 0| 30.0000  
886| 0| 3| Mr. Patrick Dooley| male| 32.0| 0| 0| 7.7500  
  
Report generated by
[YData](https://ydata.ai/?utm_source=opensource&utm_medium=pandasprofiling&utm_campaign=report).

  *[HIGH CORRELATION]: This variable has a high overall correlation with 1 fields: Survived

