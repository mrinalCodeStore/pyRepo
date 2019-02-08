import pandas as pd
import mysql.connector as cn

conn=cn.connect(host='localhost', user='root', passwd='root', database='emp')
qry1='select * from info'
df=pd.read_sql(qry1 , conn)
print(df)
