import random

#a=[int(x) for x in input().split()]
n=int(input("Enter the size of the list to sort using selection sort"))
a=random.sample(range(1,100),n)#n can have a maximum value of 99
print(a)

k=0
smallest=a[0]
for i in a:
  for j in range(k,len(a)):
    if a[k]>a[j]:
        a[k],a[j]=a[j],a[k]
        
  k=k+1

print("the sorted list is: ")
print(a)
