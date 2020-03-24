
def use1(f,a,dic):
    list = []
    str = f.read()
    list = str.split(' ')
    for i in list:
        if i in dic1:
            dic1[i] = dic1[i] + 1
        else:
            dic1[i] = 0
    a.append(sorted(dic1.items(), key=lambda x: x[1], reverse=True))
with open('a.txt','r',encoding='UTF-8') as f:
    dic1 = {}
    a = []
    use1(f,a,dic1)

with open('b.txt','r',encoding='UTF-8') as f2:
    dic2={}
    b=[]
    use1(f2,b,dic2)
sum=0
for i in range(10):
    if(a[0][i][0]==b[0][i][0]):
        sum+=10
print('is',sum,'%')




