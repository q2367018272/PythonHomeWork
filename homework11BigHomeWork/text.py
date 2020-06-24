import pymysql
from getContent import getContent
db = pymysql.connect("localhost", "root", "123456", "testdb")
cursor = db.cursor()
sql = "truncate table content"
cursor.execute(sql)