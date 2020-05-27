from multiprocessing import Pool,Manager
import time
def j_su(q):
    for i2 in range(99999):
        n=q.get()
        if(n==1):
            print('not')
        else:
            for i in range(2,n):
                if(n%i==0):
                    print(n,'not')
                    break
            else:
                print(n,'yes')

if __name__=='__main__':
    po=Pool(4)
    q=Manager().Queue()
    for i in range(1,100000):
        q.put(i)
    start_time=time.time()
    po.apply_async(j_su(q,),)
    po.close()
    po.join()
    end_time=time.time()

    four_time=end_time-start_time

    po = Pool(10)
    q = Manager().Queue()
    for i in range(1, 100000):
        q.put(i)
    start_time = time.time()
    po.apply_async(j_su(q, ), )
    po.close()
    po.join()
    end_time = time.time()

    ten_time=end_time-start_time

    print(four_time,ten_time)








'''
for i in range(1,10):
    print(i)
'''