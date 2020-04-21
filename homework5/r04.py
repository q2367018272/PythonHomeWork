import functools
def decaa(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        res=func(*args,**kw)
        print(func.__name__)
        return res
    return wrapper

@decaa
def a():
    for i in range(2,20000):
        for k in range(2,i):
            if(i%k==0 and i!=k):
                break
        else:
            print(i)
#a()
@decaa
def b(q,w):
    for i in range(q,w):
        for k in range(2,i):
            if(i%k==0 and i!=k):
                break
        else:
            print(i)

#b(2,10000)

def c(q,w):
    l=[]
    for i in range(q,w):
        for k in range(2,i):
            if(i%k==0 and i!=k):
                break
        else:
            l.append(i)
    return l

print(c(2,100))

