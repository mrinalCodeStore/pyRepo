import pandas as pd
import numpy as np
A=pd.DataFrame({"Names":["Rohan","Sila","Visal","Rahul"],"Subject1":[23,12,11,50],"Subject2":[13,25,37,19],"Subject3":[17,25,19,30]})
#A['Total']=[]
#A['Grade']=np.NaN
atotal=[]
total=[]
mrks=[]
for (row,rowSeries)in A.iterrows():
    atotal=rowSeries['Subject1']+rowSeries['Subject2']+rowSeries['Subject3']
    total.append(atotal)
    #print(total)
    c=total
    l=len(c)
   
    if atotal>=90:
       mrks.append('A+')
    elif atotal>=70:    
        mrks.append('A')
    elif atotal>=60:    
        mrks.append('B')
    elif atotal>=50:
        mrks.append('c')
    elif atotal>=40:
        mrks.append('D')    
    else:
        mrks.append('F')
        
A['Total']=total
A['Grade']=mrks

print("The record are:-")
print(A)
