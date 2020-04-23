from dog import dog
from human import human
import random
import time
human1=human()
human2=human()
dog1=dog()
dog2=dog()
dog3=dog()
humans=[human1,human2]
dogs=[dog1,dog2,dog3]
ran=random.randint(0,1)
def show():
    print('___')
    for a in humans:
        print('人',a.health,a.aggressivity)
    for b in dogs:
        print('狗',b.health,b.aggressivity)

if ran == 0:
    while(1):
        x=random.randint(0, len(humans)-1)
        y=random.randint(0, len(dogs)-1)
        dogs[y].injured(humans[x].aggressivity)
        if dogs[y].health <= 0:
            dogs.pop(y)
        if len(dogs)==0:
            print('human win')
            break



        x = random.randint(0, len(humans)-1)
        y = random.randint(0, len(dogs)-1)
        humans[x].injured(dogs[y].aggressivity)
        if humans[x].health <= 0:
            humans.pop(x)
        if len(humans)==0:
            print('dog win')
            break

        show()
        time.sleep(1)


else:
    while(1):
        x = random.randint(0, len(humans) - 1)
        y = random.randint(0, len(dogs) - 1)
        humans[x].injured(dogs[y].aggressivity)
        if humans[x].health <= 0:
            humans.pop(x)
        if len(humans) == 0:
             print('dog win')
             break

        x = random.randint(0, len(humans) - 1)
        y = random.randint(0, len(dogs) - 1)
        dogs[y].injured(humans[x].aggressivity)
        if dogs[y].health <= 0:
             dogs.pop(y)
        if len(dogs) == 0:
             print('human win')
             break

        show()
        time.sleep(1)







