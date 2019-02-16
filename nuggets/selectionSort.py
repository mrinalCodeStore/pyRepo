ls1= [int(x) for x in input("Input the array:- ").split(',')]
maxVal=0
maxIndex=0
temp=0
rg=len(ls1)
print('The entered list is;-', ls1)

for i in range(0,rg):
        for j in range(0,rg):
                if maxVal<=ls1[j]:
                        maxIndex=j
                        maxVal=ls1[j]
        temp=ls1[rg-1]
        ls1[rg-1]=maxVal
        ls1[maxIndex]=temp
        rg=rg-1
        maxVal=0
        maxIndex=0
        j=0
print('The sorted array is',ls1)

