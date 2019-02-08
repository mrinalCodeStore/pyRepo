
a=5
x=-9
b=4.5
c='Mrinal'

print(type(a)) #prints the datatype of the variable
print(type(b))  #all the data is object ...but its not strong OOP as it doesnot support strong encapsulation
print(type(c))

d=a+a

print (d)
print(type(d))

e=c+c

print(e)
print(type(e))

f=a+b   #implicit type conversion

#Python always converts smaller data type to larger data type to avoid the loss of data.

print(f)
print(type(f))

# g=a+c # no cant do

# g=str(a)+c  #Explicit type conversion
print(g)
print(type(g))
