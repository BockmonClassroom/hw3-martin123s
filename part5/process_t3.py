# Shuiming Chen
# 01/28/2025

import pandas as pd
import os


# read file from table 1 handled earlier in part 4
t1 = pd.read_csv("../part4_redo_part2_3/t1.csv")
t3 = pd.read_csv("../Data/t3_user_active_min_pre.csv")

# handle table 3 values
# drop duplicate rows just in case.
t3 = t3.drop_duplicates()

# Remove rows where active_mins is more than 12 hours
t3 = t3[t3["active_mins"] < 720]

# drop the date column in t3 in order to aggregate data
t3 = t3.drop(columns=['dt'])

# sum the user total playing time and reset index
t3 = t3.groupby("uid").sum().reset_index()

# change the column name
t3.rename(columns={"active_mins": "total_act_mins_pre"}, inplace=True)

# calculate mean and median
mean = t3["total_act_mins_pre"].mean()
median = t3["total_act_mins_pre"].median()

# Print the results
print(f"\ntable 3 has Mean = {mean:.2f}, Median = {median:.2f}\n")


# combine table 3 and table 1
data = pd.merge(t1, t3[["uid", "total_act_mins_pre"]], on="uid", how="left")
print(data.info())


# generage a new csv file and store in part 5 folder
path = os.path.join("./", "combine_t1_t3.csv")
data.to_csv(path, index=False)