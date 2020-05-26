import time
import threading
'''
def sing():
    for i in range(3):
        print('sing')
        time.sleep(1)

def dance():
    for i in range(3):
        print('dance')
        time.sleep(1)
if __name__=='__main__':
    th1=threading.Thread(target=sing)
    th2=threading.Thread(target=dance)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(len(threading.enumerate()))
'''
'''
class one(threading.Thread):
    def run(self):
        for i in range(3):
            print(self.name)
            time.sleep(1)
t=one()
t.start()
'''
'''


q=Queue(10)
for i in range(10):
    q.put(i)
while not q.empty():
    print(q.get(i))
'''
import queue
'''
q=queue.LifoQueue(10)
for i in range(10):
    q.put(i)
while not q.empty():
    print(q.get())
'''
'''
q=queue.PriorityQueue(3)
q.put((500,'a'))
q.put((3,'b'))
q.put((100,'c'))
print(q.get())
print(q.get())
print(q.get())
'''
'''
class a(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.data=queue

    def run(self):
        for i in range(100):
            self.data.put(i)
            print('cr',i)
            time.sleep(2)
class b(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.data = queue

    def run(self):
        for i in range(100):

            print(self.data.get(i))
            time.sleep(1)
q=queue.Queue()
a=a(q)
b=b(q)
a.start()
b.start()
'''

a=0
mutex=threading.Lock()
def one():
    global a
    for i in range(100000):
        mutex.acquire()
        a=a+1
        mutex.release()
    print('ond',a)
def two():
    global a
    for i in range(100000):
        mutex.acquire()
        a = a + 1
        mutex.release()
    print('two',a)

th1=threading.Thread(target=one)
th2=threading.Thread(target=two)
th1.start()
th2.start()




