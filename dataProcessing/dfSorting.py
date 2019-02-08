import pandas as pd

df=pd.read_csv("csv1.csv")
#print(df)
engMrks=df.pivot_table(index=["name"],values=["english"],aggfunc="mean")
print(type(engMrks))
print(engMrks)
engMrks.sort_values(by="english", ascending=True)
print(engMrks)