import time
from _collections import deque
list=[1,2,3]
st=time.time()
list.insert(0,0)
list.append(4)
et=time.time()
dt=et-st
print(list)
print(st,et,dt)

list2=deque()
list2.append(1)
list2.append(2)
list2.append(3)

st2=time.time()
list2.append(4)
list2.appendleft(0)
print(list2)
et2=time.time()
dt2=et2-st2
print(st2,et2,dt2)
