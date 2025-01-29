# Shuiming Chen
# 01/28/2025

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# read file from part 2 (merged one with table 1 and table 2)
df = pd.read_csv("../part2/part2.csv")


# get extream value of total playing time
max1 = df[df["variant_number"] == 0]["total_act_mins"].max()
max2 = df[df["variant_number"] == 1]["total_act_mins"].max()
print(f"\n(Group 1) Control Group: max value = {max1}")
print(f"(Group 2) Treatment Group: max value = {max2}\n")

# split the two groups
group1 = df[df["variant_number"] == 0]["total_act_mins"]
group2 = df[df["variant_number"] == 1]["total_act_mins"]
total = np.concatenate([group1, group2])

# Plot histograms
plt.figure(figsize=(10, 6))

# Total group
sns.histplot(total, bins=20, color="gray", alpha=0.7, label="Total")

# Group 1
sns.histplot(group1, bins=20, color="blue", alpha=0.7, label="Group 1")

# Group 2
sns.histplot(group2, bins=20, color="orange", alpha=0.7, label="Group 2")

# Add labels and legend
plt.title("Histogram of Total, Group 1, and Group 2", fontsize=14)
plt.xlabel("Total Active Minutes", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.legend(fontsize=12)
plt.show()