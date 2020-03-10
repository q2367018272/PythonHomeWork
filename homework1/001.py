num=[x for x in range(50) if x%2==0]
print(num)
num.clear()
num=[x for x in range(50) if x%2!=0]
print(num)
num.clear()
for i in range(2,50):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        num.append(i)
print(num)
num.clear()
num=[x for x in range(1,50) if (x%2==0)and(x%3==0)]
print(num)