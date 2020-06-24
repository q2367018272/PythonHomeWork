import requests
import re
from bs4 import BeautifulSoup

url='https://www.tianyancha.com/search?key=老八'
cookie_str=r'TYCID=19cdd080905511ea9a545d2e5fe4d195; undefined=19cdd080905511ea9a545d2e5fe4d195; ssuid=5298439832; _ga=GA1.2.1912679248.1588850579; bad_idabbf8ae0-11ae-11ea-87f8-1f7f1080a565=4ff15f61-9055-11ea-96f7-b97f34e24f52; bad_id5b882720-11af-11ea-87f8-1f7f1080a565=52e39d52-9055-11ea-800c-5db6e451bb34; jsid=SEM-BAIDU-PZ2005-SY-000001; _gid=GA1.2.1794431917.1589339443; tyc-user-phone=%255B%252215634306473%2522%255D; aliyungf_tc=AQAAAA1cgHWGzwkAEv7LG44HOmQBqHOo; csrfToken=hNs1YWrRtccwBgGltK_iKCn3; bannerFlag=false; token=67000ab008a549728510e31f34f3431b; _utm=31269aa8ffd448a69c653890cf27372d; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522vipToMonth%2522%253A%2522false%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%252210%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTYzNDMwNjQ3MyIsImlhdCI6MTU4OTM0NzMxMCwiZXhwIjoxNjIwODgzMzEwfQ.zUdjXU5sK_SKKhllK7wI2bdtfp2AsrxLJYRskidot4ro4y2iPfLpD6nRzA8RGv9NoY7Ao5g5Db-oDD8SmeJ9Ow%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%2582%2585%25E6%25AF%2585%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215634306473%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTYzNDMwNjQ3MyIsImlhdCI6MTU4OTM0NzMxMCwiZXhwIjoxNjIwODgzMzEwfQ.zUdjXU5sK_SKKhllK7wI2bdtfp2AsrxLJYRskidot4ro4y2iPfLpD6nRzA8RGv9NoY7Ao5g5Db-oDD8SmeJ9Ow; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1589347072,1589347077,1589347603,1589347867; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1589347878'
cookies={}
for line in cookie_str.split(';'):
    key,value=line.split('=',1)
    cookies[key] = value
s=requests.session()
res=s.get(url=url,cookies=cookies).text
soup=BeautifulSoup(res,'lxml')
print(soup.find(attrs={'class':'search-block header-block-container'}).find(attrs={'class':'header'}).a['href'])
res=s.get(url=url,cookies=cookies).text
soup=BeautifulSoup(res,'lxml')
print(soup.find(attrs={'class':'search-block header-block-container'}).find(attrs={'class':'header'}).a['href'])
