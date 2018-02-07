import pandas as pd
import numpy as np
import csv
import random
import itertools
# data1=pd.read_csv("height.csv")
# print(data1.head())
# print(data1.describe())

data=[5,7,8,6,4]
# answer=[]
sample=3
answer= list(itertools.combinations(data,3))
print(answer)

avg_list=[]
for i in answer:
    avg=np.average(i)
    avg_list.append(avg)
print(avg_list)

SD=np.std(avg_list)
print(SD)

df=pd.DataFrame(avg_list)
print(df)


# j=0
# for i in data:
#     if j<sample:
#         avg.append(i)
#     j=j+1
# print(avg)

# result=[]
# for j in range(1,11):
#     result1=[data[i] for i in random.sample(range(len(data)),sample)]
#     result.append(sorted(result1))
# print(result)
# print(type(result))

# count=0
# unique=[]
# for i in result:
#     if count ==0:
#         unique.append[i]
#         count +=1
#     elif count !=0:
#
#     unique=sorted(i)
# print(sorted_result)
