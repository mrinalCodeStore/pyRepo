string=input("Enter a String")
length=len(string)
maxLen=0
maxSub=''
sub=''
lenSub=0
for a in range(length):
    if string[a] in 'aeiou' or string[a] in 'AEIOU':
        if lenSub>maxLen:
            maxSub = sub
            sub=''
            lenSub=0
    else:
        sub+=string[a]
        lensub=len(sub)
    #a +=1
print("Max length substring is: ", maxSub , end='')
print("with ",maxLen,"Characters")
        
