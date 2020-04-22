class dog:
    dogs={'red':['red',80,1000],'blue':['blue',50,2000],'yellow':['yellow',40,3000]}
    def show(self):
        print('color num price')
        print(self.dogs['red'])
        print(self.dogs['blue'])
        print(self.dogs['yellow'])

    def change(self):
        a=str(input('color is:'))
        b=int(input('num is:'))
        for x,y in self.dogs.items():
            if x == a:
                y[1]=y[1]-b
                print('money is:',b*y[2])
                print('还剩下',y[1],'只',y[0],'狗')


d=dog()
d.show()
for i in range(3):
    d.change()

