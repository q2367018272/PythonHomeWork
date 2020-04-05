import os,time
files=os.listdir()
for file in files:
    if(os.path.isdir(file)):
        print('文件夹|', file, '|')
    else:
        fsize = os.path.getsize(file)
        print('文件|', file, '|', time.ctime(os.path.getmtime(file)), '|', fsize,'b')
