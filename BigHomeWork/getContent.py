import requests
from bs4 import BeautifulSoup
import lxml
import re
import json

url='http://www.nec-pbx.com/'
url2='https://www.baidu.com/'
def getContent(p,url,k):
    stringg=''
    headers = {'content-type': 'charset=ISO-8859-1'}
    response = requests.get(url,headers=headers)
    html = response.text.encode('ISO-8859-1')
    soup = BeautifulSoup(html, 'lxml')
    for a in soup.findAll(text=re.compile('(产品|服务)')):
        try:
            #print(a)
            for i,child in enumerate(a.parent.children):
                stringg=stringg+child
                print(child)
            #print(a.parent['href'])
            stringg=stringg+a.parent['href']
            if(k==1):
                stringg=stringg+getContent(p,a.parent['href'],0)
        except:
            pass
    return stringg

getContent('99999',"http://www.nec-pbx.com/",1)