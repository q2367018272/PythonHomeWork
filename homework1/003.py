num1=[x for x in range(0,100,3)]
num2=[x for x in range(0,100,2)]
set1=set(num1)
set2=set(num2)
print(sorted(set1 & set2))
