#Merge and join operation on python dataframe
import pandas as pd
df1=pd.DataFrame({'hpi':[80,90,70,60],'int_rate':[2,1,2,3],'ind_gdp':[50,45,45,67]}\
                 ,index = [2001,2002,2003,2004])
df2=pd.DataFrame({'hpi':[80,90,70,60],'int_rate':[2,1,2,3],'ind_gdp':[50,45,45,67]}\
                 ,index = [2005,2006,2007,2008])
df3=pd.DataFrame({'hpi1':[8,9,7,6],'int_rate1':[2,1,2,3],'ind_gdp1':[5,45,45,67]}\
                 ,index = [2005,2007,2007,2008])
print(df1,'\n',df2)

#merging of two or more DataFrames

merge=pd.merge(df1,df2)#merge done on the matching columns only
print(merge) 

merge1=pd.merge(df1,df2,on='hpi')#merge done on the specified column
print(merge1)


#joining of two or more DataFrames

join0=df2.join(df3) # join is done on the matching column name
print(join0)
