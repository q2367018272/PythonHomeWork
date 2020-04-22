class student:

    name = ''
    age = 0
    score = [0,0,0]

    @classmethod
    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.score=c


    @classmethod
    def get_name(cls):
        return cls.name

    @classmethod
    def get_age(cls):
        return cls.age

    @classmethod
    def get_course(cls):
        return max(cls.score)




a=student('tom',18,[10,20,30])
print(a.get_name(),a.get_age(),a.get_course())
b=student('jarry',19,[100,200,300])
print(b.get_name(),b.get_age(),b.get_course())


