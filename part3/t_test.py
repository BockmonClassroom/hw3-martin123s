# Shuiming Chen
# 01/28/2025

import pandas as pd
import scipy.stats as stats
import pingouin as pg
from statsmodels.stats.weightstats import ttest_ind


# (1) read file from part 2 (merged one with table 1 and table 2)
df = pd.read_csv("../part2/part2.csv")

# split the two groups
group1 = df[df["variant_number"] == 0]["total_act_mins"]
group2 = df[df["variant_number"] == 1]["total_act_mins"]


# Perform the two sample t-test with two groups
# Method 1: Using Scipy library for t-test
res1 = stats.ttest_ind(a=group1, b=group2, equal_var=True)

# Method 2: Two-Sample T-Test with Pingouin
res2 = pg.ttest(group1, group2, correction=True)

# Method 3: Two-Sample T-Test with Statsmodels
res3 = ttest_ind(group1, group2)

print(res1)
print("========================================\n")
print(res2)
print("========================================\n")
print(res3)