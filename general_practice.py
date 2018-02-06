import pandas as pd

df=pd.DataFrame([[1,2,3],[4,5,6],[8,7,2]])
lst=pd.DataFrame([2,7,8])
print(df)
print('..........')
print(df.shape)
print('..........')
dfm=df.max()
print(dfm)
print('..........')
df['raj']=lst
print(df)
# new_df=df.T
# new=new_df.append(lst)
# newest=new.T
# print(newest)
