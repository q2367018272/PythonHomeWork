with open('Blowing in the wind.txt','r+') as f:
    '''content=f.read()
    f.seek(0,0)
    f.write("tou\n"+content)'''
    list=[]
    for i in f.readlines():
        list.append(i)
    print(list)
    list.insert(1,"GM\n")
    list.insert(len(list),'\nLAST')
    print(list)
    sum=''
    for i in range(len(list)):
        sum=sum+list[i]
    print(sum)
    f.seek(0,0)
    f.write(sum)


