def Statistics(a):
    letter=0
    number=0
    space=0
    others=0
    for i in a:
        if i<='9' and i >='0':
            number+=1
        elif (i<='z' and i>='a')or(i<='Z' and i>='A'):
            letter+=1
        elif(i==' '):
            space+=1
        else:
            others+=1
    print("number:",number)
    print("letter:",letter)
    print("space:",space)
    print("others:",others)

a=input()
Statistics(a)