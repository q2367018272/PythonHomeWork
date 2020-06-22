import pymysql
db = pymysql.connect("localhost","root","123456","testdb" )
cursor = db.cursor()
#添加
'''
sql = "INSERT INTO rtwo (id,content,namee,time,deletee) VALUES (2,'1','1','2020-06-22 20:31:44','1')"
'''
#删除
'''
sql = "DELETE FROM rtwo WHERE id=2"
'''
#修改
'''
sql = "UPDATE rtwo SET namee = '3' WHERE namee = '1'"
'''
#查询
sql = "SELECT * FROM rtwo WHERE id = '1'"
cursor.execute(sql)
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      print(row)
except:
   print ("Error: unable to fetch data")

"""db.commit()"""

db.close()