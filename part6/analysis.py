# Shuiming Chen
# 01/28/2025

import pandas as pd


# read table 4 file
t4 = pd.read_csv("../Data/t4_user_attributes.csv")
t1_3 = pd.read_csv("../part5/combine_t1_t3.csv")

# drop duplicate rows just in case.
t4 = t4.drop_duplicates()

# get user types
types = t4.groupby(['user_type']).size().sort_values(ascending=False).reset_index(name='count')

# combine t4 with previous t1 and t3 data
t4 = pd.merge(t1_3, t4, on='uid')

# group by user types with active playing time, get the mean value 
t4 = t4.groupby('user_type')[['total_act_mins', 'total_act_mins_pre']].mean()
print(t4)


