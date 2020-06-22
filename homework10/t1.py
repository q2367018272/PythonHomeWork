import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="Lh138630",  # 数据库密码
    database="mysql"
)
#print(mydb)
mycursor = mydb.cursor()
'''
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
'''
#mycursor.execute("CREATE TABLE t1 (name VARCHAR(255), url VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)