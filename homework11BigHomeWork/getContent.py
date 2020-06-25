import requests
from bs4 import BeautifulSoup
import lxml
import re
import json


def getContent(url,k):
    global response
    stringg=''
    encode='ISO-8859-1'
    headers = {'content-type': 'charset='+encode,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3765.400 QQBrowser/10.6.4153.400'}
    try:
        response = requests.get(url,headers=headers,timeout=3)
        if(response.encoding!='ISO-8859-1'):
            encode=response.encoding
            headers = {'content-type': 'charset=' + encode}
            response = requests.get(url, headers=headers)
    except:
        if(k==1):
            return '地址无法访问'
        else:
            pass
    html = response.text.encode(encode)
    soup = BeautifulSoup(html, 'lxml')
    for a in soup.findAll(text=re.compile('(产品|服务)')):
        try:
            #print(a)
            stringg=stringg+a
            try:
                stringg=stringg+a.parent.parent.get_text()
            except:
                pass
            if(k==1):
                try:
                    stringg=stringg+getContent(url+a.parent['href'],0)
                except:
                    pass
        except:
            pass
        continue
    if(stringg=='' and k==1):
        stringg='无相关信息'
    if len(stringg)>1000:
        stringg=stringg[0:999]
    stringg=stringg.replace('\n','')
    stringg=stringg.replace(' ','')
    return stringg

#print(getContent("http://www.nec-pbx.com/",1))