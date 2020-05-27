import requests
import re
from multiprocessing import Pool,Manager,Process

def r_1(q):
    for i in range(200):
        print(q.get(), end=' ')
        try:
            res = requests.get(q.get(),timeout=3)
            print(res.status_code)
        except Exception:
            print('error')
            pass

if __name__=='__main__':
    q=Manager().Queue()
    po=Pool(5)
    with open('url_data.txt','r') as f:
        for r in f.readlines():
            url = re.match('http[^;(\n)]*', r).group(0)
            q.put(url)
    po.apply_async(r_1,(q,))
    po.close()
    po.join()





'''
        url=re.match('http[^;(\n)]*',r).group(0)
        print(url,end=' ')
        try:
            res=requests.get(url)
            print(res.status_code)
        except Exception:
            print('error')
'''

'''
print(re.match('http[^;(\n)]*','http://www.sino-tax.com; http://mail.sino-tax.com').group())
'''