def inspect(a):
    for x,y in a.items():
        if len(y)>2:
            a[x]=y[0:2]



a={2:"22",3:"333",4:"4444"}
inspect(a)
print(a)
