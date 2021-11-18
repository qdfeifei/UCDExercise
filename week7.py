import re
txt= '''asjkdhasjukds abc@gmail.com sdikfhsduhfis sdoifhisdof
xyz@gmail.com sdkihfuds sdkfjuhsduifsd a@c.com

dfkbhsdjkfh d sdkjfgsdkj
asjkdhasjukds  sdikfhsduhfis 23abc@gmail.com sdoifhisdof
xyz@gmail.com sdkihfuds a@c.com sdkfjuhsduifsd

dfkbhsdjkfh d sdkjfgsdkj
asjkdhasjukds  sdikfhsduhfis sdoifhisdof abc@gmail.com
xyz@gmail.com sdkihfuds sdkfjuhsduifsd a@c.com

dfkbhsdjkfh d sdkjfgsdkj
asjkdhasjukds abc@gmail.com sdikfhsduhfis sdoifhisdof
xyz@gmail.com sdkihfuds sdkfjuhsduifsd a@c++.com

dfkbhsdjkfh d sdkjfgsdkj'''

#find all email address
result= re.findall("\w+@\w+.\w+",txt)
print(result)

txt1='''+353-98765 4321'''
result1= re.findall("\+\d{3}-\d{5}\s\d{4}",txt1)
print(result1)


result2=re.findall("\d+-\d+","start: 4-3, registration: 10-04")
print(result2)