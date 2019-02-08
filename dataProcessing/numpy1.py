import numpy as np

lst=[12,10,6,14]
arrFrmLst=np.array(lst)
print(arrFrmLst)

data=np.loadtxt("intCSV.txt",dtype=np.uint8,delimiter=",")
print(data)
print(data.size)
print(data.shape)
print(data[2][9])
