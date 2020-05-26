import random
import threading
from queue import Queue
q=Queue(100)
for i in range(100):
    q.put(random.randint(0,99))
def run():
    for i in range(20):
        print(q.get())

t1=threading.Thread(target=run)
t2=threading.Thread(target=run)
t3=threading.Thread(target=run)
t4=threading.Thread(target=run)
t5=threading.Thread(target=run)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
