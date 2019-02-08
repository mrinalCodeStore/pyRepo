import json as jj

line="this is a great, this is awesome"

lst=line.split() #splits on the basis of space and assign them as list items

dic=dict()
for i in lst:
    key = i
    if key not in dic:
        count=lst.count(key)
        dic[key]=count
print("the word count of the text: ", dic)
print("performing pretty printing", jj.dumps(dic,indent=1))

