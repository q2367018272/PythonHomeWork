import re

list=[]
with open('r01d.txt','r',encoding='utf-8') as f:
    list=f.readlines()

strlist=[]
for str in list:
    try:
        str2 = re.search('http://((\w)|.)*\'', str).group()
        if str2:
            print(str2[:-1])
            strlist.append(str2[:-1])
    except AttributeError:
        pass

with open('r01e.txt','w',encoding='utf-8') as f:
    for str in strlist:
        f.write(str+'\n')
'''str=re.search('http://((\w)|.)*\'',"'http://www.violetshow.com');").group()
print(str[:-1])'''