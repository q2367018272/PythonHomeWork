dict={x:10*x for x in range(1,11)}
print(dict)

for k,v in dict.items():
    if(v>80):
        print(k,":",v)