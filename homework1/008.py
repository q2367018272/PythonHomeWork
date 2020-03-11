class staff:
    def __init__(self,a,b,c,d):
        self.num=a
        self.name=b
        self.year=c
        self.money=d

a=[]
b=[]
for i in range(10):
    a.append(staff(i,"a"+str(i),20+i,5000+100*i))
    b.append(a[i].money)
b.reverse()
for i in b:
    print(i,end="  ")



