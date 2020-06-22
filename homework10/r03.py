from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'rtwo'
    '''id = Column(String(20), primary_key=True)
    name = Column(String(20))'''
    id = Column(String(20), primary_key=True)
    content = Column(String(20))
    namee=Column(String(20))
    time=Column(String(20))
    deletee=Column(String(20))
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/testdb')
DBSession = sessionmaker(bind=engine)
session = DBSession()
#插入
'''
new_user = User(id='2', content='2',namee='2',time='2020-06-22 21:22:07',deletee='2')
session.add(new_user)
'''
#查询
'''
user = session.query(User).filter(User.id=='2').one()
print('type:', type(user))
print('name:', user.namee)
'''
#更新
'''
result = session.query(User).filter(User.id == '2').first()
result.namee = '30'
'''
#删除
'''
result = session.query(User).filter(User.id == '2').first()
session.delete(result)
'''
session.commit()
session.close()

