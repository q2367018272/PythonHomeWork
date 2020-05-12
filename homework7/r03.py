import requests
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import quote
url='http://www.listeningexpress.com/studioclassroom/ad/'
res=requests.get(url).text
list=[]
soup=BeautifulSoup(res,'lxml')
for id in soup.select('#proglist'):
    for a in id.select('a'):
        list.append(a['href'])
list2=[]

for k in list:
    list2.append(re.search('sc-ad[^\']*\'',k).group()[:-1])
print(list2)

key=0

for k in list2:
    url2=url+quote(k)
    res2=requests.get(url2)
    with open('music/r03('+str(key)+').mp3', 'wb') as f:
        f.write(res2.content)
        key=key+1


'''
print(res.content)
with open('music/r03.mp3','wb') as f:
    f.write(res.content)
'''
'''javascript:p('sc-ad 2020-05-02 Life Hacks.mp3');'''