import pymysql

def select_name():
    conn = pymysql.connect(host='localhost', user='root', password='0913', db='date20200115', charset='utf8')
    cur = conn.cursor()
    sql = 'select name from t_music'
    cur.execute(sql)
    content = cur.fetchall()
    return content


def select_path(music_name):
    conn = pymysql.connect(host='localhost', user='root', password='0913', db='date20200115', charset='utf8')
    cur = conn.cursor()
    sql = "select path from t_music where name='{}'".format(music_name)
    cur.execute(sql)
    content = cur.fetchall()
    return content
