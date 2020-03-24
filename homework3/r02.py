import io
list=[]
k=1
with open('input.txt','r') as f:
    for i in f.readlines():
        list.append(i)
for m in list:
    print(k,'. ',m,end='')
    k+=1
