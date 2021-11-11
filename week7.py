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
xyz@gmail.com sdkihfuds sdkfjuhsduifsd a@c.com

dfkbhsdjkfh d sdkjfgsdkj'''

result= re.findall("\w+@\w+.\w+",txt)
print(result)