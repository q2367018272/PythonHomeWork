class student:

    def __sum(self):
        return self.__english+self.__math+self.__chinese
    def __avg(self):
        return self.__sum()/3

    def __init__(self,name,age,sex,english,math,chinese):
        self.__name=name
        self.__age=age
        self.__sex=sex
        self.__english=english
        self.__math=math
        self.__chinese=chinese
        self.__sum2=self.__sum()
        self.__avg2=self.__avg()

    def show(self):
        print('\n'.join(['%s:%s' % item for item in self.__dict__.items()]))

a=student('a',5,'man',10,20,30)
a.show()