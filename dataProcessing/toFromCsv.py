import pandas as pd

df = pd.read_csv("csv1.csv") #1st row of csv data as dataframe header
print(df)

print('-------------------------------------------------------------')
df = pd.read_csv("csv2.csv",names=['Name','Roll','Age'])#custome dataframe header
print(df)

print('-------------------------------------------------------------')
df = pd.read_csv("csv2.csv",header=None)#0,1,2,3,4 as dataframe header
print(df)

print('-------------------------------------------------------------')
df = pd.read_csv("csv2.csv",header=None, skiprows=1)#skips one row from the begining of the csv file
print(df)

df1=pd.DataFrame([[1,2,3],[4,5,6]],columns=['1st','2nd','3rd'])
print(df1)

df1.to_csv("csv3.csv")
