import os
import pickle
class student:
    name=' '
    number=' '
    suc=0
    def __init__(self,a,b,c):
        self.name=a
        self.number=b
        self.suc=c

a=student('张三','101',78)
b=student('李四','102',87)
c=student('王五','103',83)

with open('student.pkl','wb') as f:
    pickle.dump(a,f)
    pickle.dump(b, f)
    pickle.dump(c, f)

with open('student.pkl','rb') as m:
    aa=pickle.load(m)
    bb=pickle.load(m)
    cc=pickle.load(m)
list1=[aa,bb,cc]
list1.sort(key=lambda x:x.suc,reverse=True)
print(list1)
for i in list1:
    print(i.name,' ',i.number,' ',i.suc)

with open('student2.pkl','wb') as f:
    pickle.dump(aa,f)
    pickle.dump(bb, f)
    pickle.dump(cc, f)

