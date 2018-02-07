import pandas as pd
import itertools

raw=pd.read_csv("avg_5_samplev2.csv")
print(raw)

# df=pd.DataFrame([[1,2,3,5],[4,5,6,6],[8,7,2,8]])
# lst=pd.DataFrame([2,7,8,5])
# print(df)
# print('..........')
# print(df.shape)
# print('..........')
# dfm=df.max()
# print(dfm)
# print('..........')
# df['raj']=lst
# print(df)
# sample=2
# df_itt=pd.DataFrame()
# # for col in df.columns:
# #     les = list(itertools.combinations(df,sample))
# #     print(les)
# #     print("............")
# # itt_list=list(itertools.combinations(df[1],sample))
# # print(itt_list)
# for i in itertools.combinations(df[1],sample):
#     df_itt.append(list(i))
# print(df_itt)
#     # print(all_possible_samples)
#     # print(type(all_possible_samples))
#     plt1_sam=pd.DataFrame.from_records(all_possible_samples)
#     plt1_avg_sam = plt1_sa

# new_df=df.T
# new=new_df.append(lst)
# newest=new.T
# print(newest)
