import sys
a=''
while a != "y":
    try:
        a=int(input("enter a number"))   
        count=0
        for i in range(2,a):
            if a%i==0:
                count=count+1
        if count>=2:
            print("the number is not prime")
        else:
            print("the number is prime")
    except:
        sys.exit()
