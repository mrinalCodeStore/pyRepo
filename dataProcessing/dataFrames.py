import pandas as pd

#Creating a DataFrame from nested dictionary as single dictionary cant be used
dic={"col1":{"fname":"mrinal","lname":"debnath","marks":98}}
df=pd.DataFrame(dic)
print(df,'\n')
print(df.col1['fname'],'\n') #Accessing a single element
print(df['col1'],'\n') #Accessing a entire column
print(df['fname':'lname'],'\n')

#creating a DataFrame from a normal List and providing a index and column
lst=['a','b','c','d','e']

df1=pd.DataFrame(lst,index=['1','2','3','4','5'],columns=['col1'])
print(df1,'\n')

sales=[('a','b'),('c','d'),('e','f')]
labels=[5,6]
df2=pd.DataFrame(sales,columns=labels)

print(df2)

sales1=[(5,['a','b']),(6,['c','d'])]
df3=pd.DataFrame(sales1,index=[7, 8],columns=[2,3])

print(df3)
