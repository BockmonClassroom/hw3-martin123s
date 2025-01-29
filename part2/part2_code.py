# Shuiming Chen
# 01/27/2025

import pandas as pd
import os


# read these two files
t1 = pd.read_csv("../Data/t1_user_active_min.csv")
t2 = pd.read_csv("../Data/t2_user_variant.csv")

# (1) handling table 1:
# drop duplicate rows just in case.
t1 = t1.drop_duplicates()

# drop the date column in t1 in order to aggregate data
t1 = t1.drop(columns=['dt'])

# sum the user total playing time and reset index
t1 = t1.groupby("uid").sum().reset_index()

# change the column name
t1.rename(columns={"active_mins": "total_act_mins"}, inplace=True)


# (2) handling table 2:
# drop duplicate rows just in case.
t2 = t2.drop_duplicates()

# merge the data of t1 and t2
data = pd.merge(t1, t2[["uid", "variant_number"]], on="uid", how="left")
print(data.head())



# (3) generage a new csv file and store in part 2 folder
path = os.path.join("./", "part2.csv")
data.to_csv(path, index=False)



