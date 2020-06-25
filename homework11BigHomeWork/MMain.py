from geturl import geturl
from getContent import getContent
from multiprocessing import Pool,Manager
import pymysql

#Mysql 里面testdb库有一个已经建好的库，叫Content
def ToMysql(q):
    db = pymysql.connect("localhost", "root", "123456", "testdb")
    cursor = db.cursor()
    while (q.empty):
        str = q.get()
        str = str.split(' ')
        sql = "SELECT enterpriseName FROM temp_icp_web2 where autoID = %s"
        cursor.execute(sql, int(str[0]))
        result = cursor.fetchone()
        print(str[0],'内容获取...')
        str.append(getContent(str[1],1))
        print(str[0],'爬取完成，读入数据库...')
        sql = "INSERT INTO Content (id,company,url,content) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql,(int(str[0]),result[0],str[1],str[2]))
        db.commit()
        print(str[0],'读入成功')
    db.close()


if __name__=='__main__':
    db = pymysql.connect("localhost", "root", "123456", "testdb")
    cursor = db.cursor()
    sql = "truncate table content"
    cursor.execute(sql)
    db.close()
    po = Pool(8)
    q = Manager().Queue()
    list = geturl()
    for key, value in list.items():
        q.put(str(key) + ' ' + value)
    for i in range(8):
        po.apply_async(ToMysql, (q,))
    po.close()
    po.join()



'''
print(getContent('99999',"http://www.nec-pbx.com/",1))
'''