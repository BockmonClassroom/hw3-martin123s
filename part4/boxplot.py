# Shuiming Chen
# 01/28/2025

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# read file from part 2 (merged one with table 1 and table 2)
df = pd.read_csv("../part2/part2.csv")

# define the figure size
plt.figure(figsize=(10, 8))

# create a boxplot
sns.boxplot(x='variant_number', y='total_act_mins', data=df)
plt.title("users total playing time by groups")
plt.xlabel('by groups')
plt.ylabel('playing time')
plt.show()