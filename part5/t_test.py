# Shuiming Chen
# 01/28/2025

import pandas as pd
import scipy.stats as stats
import pingouin as pg
from statsmodels.stats.weightstats import ttest_ind


# read file from new table combine_t1_t3.csv file
df = pd.read_csv("combine_t1_t3.csv")

# split the two groups
group1 = df[df["variant_number"] == 0]
group2 = df[df["variant_number"] == 1]



# (1) handle control group
# get group 1 data sets
group1_set1 = group1[["uid", "total_act_mins"]]["total_act_mins"]
group1_set2 = group1[["uid", "total_act_mins_pre"]]["total_act_mins_pre"]

# Perform the two sample t-test with different methods
# Method 1: Using Scipy library for t-test
group1_res1 = stats.ttest_ind(a=group1_set1, b=group1_set2, equal_var=True)

# Method 2: Two-Sample T-Test with Pingouin
group1_res2 = pg.ttest(group1_set1, group1_set2, correction=True)

# Method 3: Two-Sample T-Test with Statsmodels
group1_res3 = ttest_ind(group1_set1, group1_set2)





# handle treatment group
# get group 2 data sets
group2_set1 = group2[["uid", "total_act_mins"]]["total_act_mins"]
group2_set2 = group2[["uid", "total_act_mins_pre"]]["total_act_mins_pre"]

# Perform the two sample t-test with different methods
# Method 1: Using Scipy library for t-test
group2_res1 = stats.ttest_ind(a=group2_set1, b=group2_set2, equal_var=True)

# Method 2: Two-Sample T-Test with Pingouin
group2_res2 = pg.ttest(group2_set1, group2_set2, correction=True)

# Method 3: Two-Sample T-Test with Statsmodels
group2_res3 = ttest_ind(group2_set1, group2_set2)


# print out results of t-test
print("\n\n(1) Results for control group\n")
print(group1_res1)
print("========================================\n")
print(group1_res2)
print("========================================\n")
print(group1_res3)


print("\n\n(2) Results for treatment group\n")
print(group2_res1)
print("++++++++++++++++++++++++++++++++++++++++\n")
print(group2_res2)
print("++++++++++++++++++++++++++++++++++++++++\n")
print(group2_res3)