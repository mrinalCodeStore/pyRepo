def rangeN(a, b):
    i=a
    while(i<b):
        yield i
        i+=1


for i in rangeN(1,6):
    print(i)
