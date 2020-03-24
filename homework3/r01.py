import io
list=[]
str=input('输入：')
while str!='':
    list.append(str)
    str=input()
print(list)
with open('input.txt','w') as f:
    for i in list:
        f.write(i+'\n')
