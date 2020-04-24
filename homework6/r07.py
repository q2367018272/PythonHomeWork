import pickle


class student:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d


while(1):
    print('增加请输入 1')
    print('删除请输入 2')
    print('修改请输入 3')
    print('查找请输入 4')
    print('查看全部请输入 5')

    sr=int(input('输入:'))
    if(sr==1):
        a=input('输入学号:')
        b=input('输入班级:')
        c=input('输入姓名:')
        d=input('输入成绩:')
        stu=student(a,b,c,d)
        stulist=[]
        with open('data_student.pkl', 'rb') as f:
            try:
                stulist = pickle.load(f)
            except EOFError:
                pass
        stulist.append(stu)
        with open('data_student.pkl', 'wb') as f:
            pickle.dump(stulist,f)
        sr=input('ok 回车')

    elif(sr==5):
        with open('data_student.pkl','rb') as f:
            stulist=pickle.load(f)
            print('num is:',len(stulist))
            for stu in stulist:
                print(stu.a,stu.b,stu.c,stu.d)
            sr = input('回车继续')


    elif(sr==4):
        sr=input('输入学号:')
        with open('data_student.pkl', 'rb') as f:
            stulist = pickle.load(f)
            for stu in stulist:
                if(sr==stu.a):
                    print('is:',stu.a,stu.b,stu.c,stu.d)
                    break
            else:
                print('not found')
        sr=input('ok 回车')

    elif(sr==2):
        sr = input('输入学号:')
        stulist=[]
        i=-1
        with open('data_student.pkl', 'rb') as f:
            stulist=pickle.load(f)
        for k in stulist:
            i=i+1
            if(k.a==sr):
                stulist.pop(i)
                break
        else:
            print('not found')
        with open('data_student.pkl', 'wb') as f:
            pickle.dump(stulist,f)
        print('ok enter')

    elif(sr==3):
        sr = input('输入修改的学号:')
        sra=input('输入修改后学号:')
        srb = input('输入修改后班级:')
        src = input('输入修改后姓名:')
        srd = input('输入修改后成绩:')
        stulist = []
        i = -1
        with open('data_student.pkl', 'rb') as f:
            stulist = pickle.load(f)
        for k in stulist:
            i = i + 1
            if (k.a == sr):
                stulist[i].a=sra
                stulist[i].b=srb
                stulist[i].c=src
                stulist[i].d=srd
                break
        else:
            print('not found')
        with open('data_student.pkl', 'wb') as f:
            pickle.dump(stulist, f)
        print('ok enter')




















