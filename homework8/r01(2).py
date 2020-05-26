from multiprocessing import Pool,Manager
import os
def reader(q):
    for i in range(20):
        print(os.getpid(),q.get())

if __name__=="__main__":
    po=Pool(5)
    q=Manager().Queue()
    for i in range(100):
        q.put(i)
    for i in range(5):
        po.apply_async(reader,(q,))
    po.close()
    po.join()

