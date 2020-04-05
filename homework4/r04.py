import hashlib
import pickle

class yh:
    xm=''
    zh=''
    mm=''
    def __init__(self,a,b,c):
        self.xm=a
        self.zh=b
        self.mm=c

yhlist=[]
with open('data4.pkl','rb') as f:
    for i in range(3):
        yhlist.append(pickle.load(f))


sr_zh=input('zh:')
sr_mm=input('mm:')

sr_zh=str(sr_zh)
sr_mm=str(sr_mm)

sr_md=hashlib.md5()
sr_md.update(sr_mm.encode('utf-8'))
sr_mm=sr_md.hexdigest()

for i in yhlist:
    if(sr_zh==i.zh):
        if(sr_mm==i.mm):
            print('success')
            break
        else:
            print('mm error')
else:
    print('zh error')




