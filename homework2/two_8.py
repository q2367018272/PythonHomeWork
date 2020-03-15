def sum(a):
    b={}
    for i in a:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
    print(b)
    for x,y in b.items():
        if y==max(b.values()):
            print(x,":",y)
a=input("输入字符串：")
sum(a)