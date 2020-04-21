import functools
name='abcde'
password='12345'
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        srname=str(input('name:'))
        srpassword=str(input('password:'))
        if((name==srname)and(password==srpassword)):
            func()
        else:
            print('no')

    return wrapper

@decorator
def test():
    print('success')
test()


