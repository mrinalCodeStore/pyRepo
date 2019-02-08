import pandas as pd

we_dic={'day':[1,2,3,4,5,6],"visitor":[1000,700,6000,1000,400,350],'bounce_rate'\
        :[20,20,23,25,10,34]}
df=pd.DataFrame(we_dic,index = [0,1,2,3,4,5])
print(df)

#operation on pandas dataFrame

#slicing
print(df.loc[0:6,'day':'bounce_rate']) #entire dataframe
print(df.loc[3:6,'visitor':'bounce_rate']) #part of the dataframe
print(df.loc[0:1,:])#two row of the dataframe
print(df.loc[:,'visitor':'bounce_rate']) #two column of the dataframe



