# Shuiming Chen
# 01/28/2025

import pandas as pd


# read file from data
t1 = pd.read_csv("../Data/t1_user_active_min.csv")

# get the max value
max_t1 = t1["active_mins"].max();
print(f"highest value in table 1 is: {max_t1}")

# calculate how many rows are beyond the daily limit
number_beyond = t1[t1["active_mins"] >= 24*60]["uid"].count()
print(f"how many dataset are there in table 1 which is not a correct value: {number_beyond}")
