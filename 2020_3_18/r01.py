import os
import pickle
data1=[x for x in range(10)]
data2={x:y for x in range(11,20) for y in range(21,30)}
with open('data.pkl','wb') as f:
    pickle.dump(data1,f)
    pickle.dump(data2,f)

with open('data.pkl','rb') as m:
    data3=pickle.load(m)
    data4=pickle.load(m)
    print(data3)
    print(data4)


