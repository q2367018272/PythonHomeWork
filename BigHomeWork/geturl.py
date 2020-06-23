import pymysql
import re

#root@localhost用户 密码为123456 数据库为testdb 表为temp_icp_web2 亲测在本机有效

def geturl():
    db = pymysql.connect("localhost", "root", "123456", "testdb")
    cursor = db.cursor()
    sql = "SELECT * FROM temp_icp_web2"
    cursor.execute(sql)
    list={}
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            try:
                list[row[3]]=re.search('(www|http)[^;(\n)]*',row[4]).group().replace('：',':')
            except:
                print(row[0],'位置',row[3],'地址异常')
            continue
    except:
        pass
    db.close()
    return list


