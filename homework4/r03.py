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
for i in range(3):
    xm=input('xm:')
    zh=input('zh:')
    mm=input('mm:')
    yh1=yh(xm,zh,mm)
    md5=hashlib.md5()
    md5.update((yh1.mm).encode('utf-8'))
    yh1.mm=md5.hexdigest()
    yhlist.append(yh1)


with open('data4.pkl','wb') as f:
    for i in yhlist:
        pickle.dump(i,f)

with open('data4.pkl','rb') as f:
    for i in range(3):
        yh11=pickle.load(f)
        print(yh11.mm)

