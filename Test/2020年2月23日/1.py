import pymysql

cur = None
conn = None


def getall(sql):  # 用来执行查询
    # 连接数据库
    conn = pymysql.connect(host='localhost', user='root', password='123123', db='test1', charset='utf8')
    cur = conn.cursor()  # 获取cursor对象
    # 通过cursor的对象去执行SQL语句
    cur.execute(sql)
    return cur.fetchall()


def exceDML(sql):  # 用来执行插入
    conn = pymysql.connect(host='localhost', user='root', password='123123', db='test1', charset='utf8')
    cur = conn.cursor()
    # 通过cursor的对象去执行SQL语句
    cur.execute(sql)
    # 提交事物
    conn.commit()


def close():  # 用来关闭连接

    if cur:
        cur.close()
    if conn:
        conn.close()
