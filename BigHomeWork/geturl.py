import pymysql
import re
import pymysql
#root@localhost用户 密码为123456 数据库为testdb 表为temp_icp_web2 亲测在本机有效


def geturl():
    print('正在提取url...')
    db = pymysql.connect("localhost", "root", "123456", "testdb")
    cursor = db.cursor()
    sql = "SELECT * FROM temp_icp_web2"
    list={}
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            try:
                list[row[0]]=re.search('(www|http)[^;(\n)]*',row[4]).group().replace('：',':')
            except:
                sql = "INSERT INTO Content (id,company,url,content) VALUES (%s,%s,%s,%s)"
                cursor.execute(sql,(int(row[0]),row[3],'地址有误','地址有误'))
                db.commit()
                #print(row[0],'位置',row[3],'地址异常')
            continue
    except:
        pass
    db.close()
    print('提取url完成...')
    return list


