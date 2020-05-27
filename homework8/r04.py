from multiprocessing import Pool,Manager,Process,Queue




def sc(q):
    while(1):
        print(q.get())

if __name__=='__main__':
    q=Queue()
    srd=''
    p2=Process(target=sc, args=(q,))
    p2.start()
    while(1):
        srd=input('')
        q.put(srd)

