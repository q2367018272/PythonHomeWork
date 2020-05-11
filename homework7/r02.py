import requests
from bs4 import BeautifulSoup
import lxml
import re
import json

def use(url):
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html,'lxml')
    list={}
    for a in soup.findAll('a'):
        if a.find_all(text=re.compile('企业')):
            list[a.string]='http://www.chrtc.cn/'+a['href']
        if a.find_all(text=re.compile('公司')):
            list[a.string]='http://www.chrtc.cn/'+a['href']
        if a.find_all(text=re.compile('关于')):
            list[a.string]='http://www.chrtc.cn/'+a['href']
        if a.find_all(text=re.compile('我们')):
            list[a.string]='http://www.chrtc.cn/'+a['href']
        if a.find_all(text=re.compile('发展')):
            list[a.string]='http://www.chrtc.cn/'+a['href']
        if a.find_all(text=re.compile('历史')):
            list[a.string]='http://www.chrtc.cn/'+a['href']
        if a.find_all(text=re.compile('概况')):
            list[a.string]='http://www.chrtc.cn/'+a['href']
    titlestring=soup.title.string
    titlestring2=titlestring.split()[0]
    with open('r02de.txt','a') as f:
        f.write(titlestring2+'\n'+str(list)+'\n')
    print(titlestring2)

with open('r01e.txt','r',encoding='UTF-8') as f:
    lines=f.readlines()
    for line in lines:
        one=re.match('http[^;(\n)]*',line)
        string=one.group().replace('\n','')
        try:
            use(string)
        except Exception:
            pass

