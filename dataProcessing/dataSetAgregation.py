import pandas as pd

df=pd.read_csv("csv1.csv")
dtGp=list(df.groupby("name"))
print(type(df.groupby("name")))
print("------------------------------------------------------")
print(type(dtGp[0]))
print('------------------------------------------------------')
print(dtGp[0])
print('------------------------------------------------------')
print(dtGp[0][0])
print('------------------------------------------------------')
print(dtGp[0][1])
print('------------------------------------------------------')
print(type(dtGp[0][1]))
print(dtGp[0][1])
print('------------------------------------------------------')
df1=dtGp[0][1]
print(df1.T)
print('------------------------------------------------------')
print(df1.loc[5:5,'name':'english'])