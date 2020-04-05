from datetime import datetime,date
def a(time):
    week=datetime.strptime(time,'%Y%m%d').weekday()+1
    week2=date(int(time[0:4]),int(time[4:6]),int(time[6:8])).isocalendar()[1]
    print(week)
    print(week2)
    school_week2=week2-7
    print('sc:',school_week2)


time = input('sr:')
a(time)