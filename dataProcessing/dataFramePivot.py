import pandas as pd

df=pd.read_csv('csv1.csv')
print(df)
#print(df)
#df2=pd.DataFrame(df.T) #tranpose the dataframe i.e. rows into column 
#print(df2)

print(df.sort_values(by='name'))

print(df.pivot_table(index=['name','stream'],aggfunc='mean'))
