import pickle
class stu:
    num=''
    name=''
    py=0
    def __init__(self,a,b,c):
        self.num=a
        self.name=b
        self.py=c


a1=stu('001','黄一',20)
a2=stu('002','黄二',10)
a3=stu('003','黄三',40)
a4=stu('004','黄四',30)
a5=stu('005','黄五',60)
a6=stu('006','黄六',50)
a7=stu('007','黄七',80)
a8=stu('008','黄八',70)
a9=stu('009','黄九',50)
aa=stu('010','黄十',49)

with open('data03.pkl','wb') as f:
    pickle.dump(a1,f)
    pickle.dump(a2, f)
    pickle.dump(a3, f)
    pickle.dump(a4, f)
    pickle.dump(a5, f)
    pickle.dump(a6, f)
    pickle.dump(a7, f)
    pickle.dump(a8, f)
    pickle.dump(a9, f)
    pickle.dump(aa, f)

list=[]
with open('data03.pkl','rb') as f:
    for i in range(10):
        data=pickle.load(f)
        list.append(data)
        'print(data.num,' ',data.name,' ',data.py)'

list.sort(key=lambda x:x.py)
for i in list:
    print(i.num,i.name,i.py)





