import random
def aa(b):
    for i in b:
        if i%2!=0:
            print(i,end=" ")
a=[random.randint(1,100) for i in range(10)]
print(a)
aa(a)
