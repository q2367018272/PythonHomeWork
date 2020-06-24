import re
from multiprocessing import Pool,Manager
import time
from geturl import geturl

def ToMysql(q):
    while(q.empty):
        str=q.get()
        str=str.split(' ')





if __name__=='__main__':
    po = Pool(4)
    q = Manager().Queue()
    list=geturl()
    for key,value in list.items():
        q.put(str(key)+' '+value)
    ToMysql(q)

