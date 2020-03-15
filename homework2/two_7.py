import random
def judge(a):
    b=[]
    for i in a:
        if i >=90:
            b.append("A")
        elif i >=80:
            b.append("B")
        elif i>=70:
            b.append("C")
        else:
            b.append("D")
    print(b)
a=[random.randint(1,100) for i in range(20)]
print(a)
judge(a)