import pymysql
cur = None
conn = None

def getall(dbname,sql):
    global cur
    #连接数据库
    conn = pymysql.connect(host = 'localhost',user = 'root',password='0913',db = dbname,charset = 'utf8')
    cur = conn.cursor()
    cur.execute(sql)
    print(cur.fetchall())
    return cur.fetchall()

def exceDML(dbname,sql):
    conn = pymysql.connect(host='localhost', user='root', password='0913', db=dbname, charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def close():
    if cur:
        cur.close()
        print('已关闭')

