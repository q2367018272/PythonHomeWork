import os
os.chdir('img')
path=os.getcwd()
for name in os.listdir(path):
    if(name[-3:]=='png'):
        name2=name
        name=name.replace('png','jpg')
        os.rename(path+'\\'+name2,path+'\\'+name)


