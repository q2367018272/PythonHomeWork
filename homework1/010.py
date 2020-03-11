dict={}
txt=open("d:/test.txt")
sr=txt.read()
list=sr.split()
print(list)
for i in list:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=int(1)
print(dict)
txt.close()