import requests
from bs4 import BeautifulSoup

url='https://www.programcreek.com/python/index/221/requests'
res=requests.get(url).text
soup=BeautifulSoup(res,'lxml')
list=[]
for aa in soup.find_all(attrs={'id':'api-list-apiname'}):
    list.append(aa.a['href'])


def one(url):
    res=requests.get(url).text
    soup=BeautifulSoup(res,'lxml')
    for a2 in soup.find_all(attrs={'class':'examplebox'}):
        print(a2.find(attrs={'class':'exampleboxbody'}).pre.text)
        with open('r04de.txt','a',encoding='utf-8') as f:
            f.write('\n'+a2.find(attrs={'class':'exampleboxbody'}).pre.text+'\n')


for k in list:
    one(k)

