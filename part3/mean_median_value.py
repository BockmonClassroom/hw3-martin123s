# Shuiming Chen
# 01/27/2025

import pandas as pd


# read file from part 2 (merged one with table 1 and table 2)
df = pd.read_csv("../part2/part2.csv")

# calculate mean and median of two groups
group_1_mean = df[df["variant_number"] == 0]["total_act_mins"].mean()
group_1_median = df[df["variant_number"] == 0]["total_act_mins"].median()

group_2_mean = df[df["variant_number"] == 1]["total_act_mins"].mean()
group_2_median = df[df["variant_number"] == 1]["total_act_mins"].median()

# Print the results
print(f"\n(Group 1) Control Group: Mean = {group_1_mean:.2f}, Median = {group_1_median:.2f}")
print(f"(Group 2) Treatment Group: Mean = {group_2_mean:.2f}, Median = {group_2_median:.2f}\n")