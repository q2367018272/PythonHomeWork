def aa():
    x=0
    def bb():
        nonlocal x
        x=x+1
        return x
    return bb
h=aa()
print(h())
print(h())