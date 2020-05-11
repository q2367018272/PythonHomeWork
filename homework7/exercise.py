import urllib.request
import urllib.parse
import urllib.error
import socket
'''get
response=urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode("utf-8"))
'''

'''post
data=bytes(urllib.parse.urlencode({'a':'1'}),encoding="utf-8")
response=urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode("utf-8"))
'''

'''time out error
try:
    response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('time out')
'''


'''response=urllib.request.urlopen("http://www.python.org")
print(response.status)
print(response.getheaders())
print(response.getheader('User-Agent'))'''


'''
request=urllib.request.Request('http://python.org')
response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
'''


'''user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
headers={'User-Agent':user_agent,'Host':'httpbin.org'}
dict={'a':'1'}
data=bytes(urllib.parse.urlencode(dict),encoding='utf-8')
request=urllib.request.Request(url="http://httpbin.org/post",headers=headers,data=data,method='POST')
response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
print(response.getheaders())'''

'''req=urllib.request.Request()
req.add_header()'''

import http.cookiejar

'''cookie=http.cookiejar.CookieJar()
handle=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handle)
response=opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name,item.value)'''

'''filename='cookle.txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
handle=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handle)
response=opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
'''
'''
filename='cookle.txt'
cookie=http.cookiejar.MozillaCookieJar()
cookie.load('cookle.txt',ignore_expires=True,ignore_discard=True)
handle=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handle)
response=opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
'''

import urllib.error
'''
try:
    response=urllib.request.urlopen('http://www.baidu21312.com')
except urllib.error.HTTPError as e:
    print(e.reason,e.code,e.headers)
except urllib.error.URLError as e:
    print(e.reason)
else:
    print('success')
'''
import urllib.parse
'''
result=urllib.parse.urlparse("http://www.baidu.com")
print(result)
'''
'''
data=['http','www.baidu.com','index.html','user','a=6','common']
print(urllib.parse.urlunparse(data))
'''
import requests
'''
response=requests.get('http://httpbin.org/get')
print(response.text)
'''
'''
data={'a':1,'b':2}
response=requests.get('http://httpbin.org/get',params=data)
print(response.text)
'''
'''
response=requests.get('http://httpbin.org/get')
print(response.text,end='\n---------\n')
print(response.json())
'''
'''
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
}
response=requests.get('http://www.tianyancha.com',headers=headers)
print(response.text)
'''

import re

result=re.match('http[^;(\n)]*','http://www.stwt.cn; http://www.erpcrm400.com')
print(type(result.group()))