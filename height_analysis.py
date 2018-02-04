import numpy as np
import random
import itertools
# import Tkinter
import matplotlib.pyplot as plt

plot3=[118,160,135,142,128,156,155,173,150,167,167,163,152,145,114,133,136,163,157,161]
pop_avg=np.average(plot3)
# print(type(pop_avg))
pop_std=np.std(plot3)
# print(type(pop_std))
print("pop_avg: %s and pop_std: %s",(pop_avg, pop_std))
# print("pop_std: ",pop_std)
sample=5
sampled_data= list(itertools.combinations(plot3,sample))
# print(sampled_data)
avg_list=[]
for i in sampled_data:
    avg_list.append(np.average(i))
print(avg_list)
plt.hist(avg_list,bins=50, color='r', histtype="step")
plt.show()

# sample_overall_avg=np.average(avg_list)
# print("Overall average: ",sample_overall_avg)
# SD=np.std(avg_list)
# print("Std of the avg_samples: ",SD)

# ax.hist(data,bins=100,range=(minimum,maximum),facecolor="r", histtype = 'step')
