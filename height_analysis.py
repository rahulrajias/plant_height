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
sample=5
# all_possible_samples = list(itertools.combinations(csv_data['1'],sample))
all_possible_samples = list(itertools.combinations(csv_data['1'],sample))
print(all_possible_samples)
print(type(all_possible_samples))
plt1_sam=pd.DataFrame.from_records(all_possible_samples)
plt1_avg_sam = plt1_sam.mean(axis=1)
print("......................")
print(type(plt1_avg_sam))

avg_sam_5=pd.DataFrame()
print(type(avg_sam_5))
avg_sam_5['plot_1'] = plt1_avg_sam
print(avg_sam_5)
