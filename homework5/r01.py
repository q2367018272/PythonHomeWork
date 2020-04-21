import time
import functools
def dec(fn):
    @functools.wraps(fn)
    def wrap(*args,**kw):
        start_time=time.time()
        res=fn(*args,**kw)
        print(fn.__name__,time.time()-start_time)
        return res
    return wrap

@dec
def test(n):
    time.sleep(n)
    print('over')

test(3)
print(test(3))






