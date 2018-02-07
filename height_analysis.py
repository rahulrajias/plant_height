import numpy as np
import random
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import csv

csv_data= pd.read_csv("Corn_Height.csv")
print(csv_data)
data_stats=csv_data.describe()
print(data_stats)
data_avg=csv_data.mean()
data_std=csv_data.std()
sample=10
all_possible_samples = list(itertools.combinations(csv_data['9'],sample))
# print(all_possible_samples)
# print(type(all_possible_samples))
plt1_sam=pd.DataFrame.from_records(all_possible_samples)
plt1_avg_sam = plt1_sam.mean(axis=1)
# print(plt1_avg_sam)
# plt1_avg_sam.to_csv("rahul1.csv")
# print("......................")
# print(type(plt1_avg_sam))
# avg_sam_5=pd.DataFrame(plt1_avg_sam)
# plt1_avg_sam5=avg_sam_5
# print(plt1_avg_sam5)

old=pd.read_csv("rahul1.csv")
new=pd.concat([old,plt1_avg_sam], axis=1)
print(new)
new.to_csv("rahul1.csv")

# print(avg_sam_5)
# print(type(avg_sam_5))
# pd.concat([plt1_avg_sam5,avg_sam_5])
# avg_sam_5.append(plt1_avg_sam)
# print(avg_sam_5)
