import re
st=' the mail is send2mrinal@gmail.com  and binarybits64@gmail.com'

res=re.findall(r'\w*@\w*.com',st)
print(res)