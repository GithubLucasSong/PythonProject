from socket import *
from threading import Thread
import pymysql


def new_thread(new_socket,new_addr):
    while True:
        sql = 'select name from t_music'
        cur.execute(sql)
        content = cur.fetchall()
        content_lis = []
        for (i,) in content:
            content_lis.append(i)
        senddata = str(content_lis)
        new_socket.send(f"请输入歌名\n{senddata}".encode())
        recvdata = new_socket.recv(1024)
        music_name = str(recvdata.decode())
        sql = "select path from t_music where name='{}'".format(music_name)
        cur.execute(sql)
        content = cur.fetchall()
        music_path = content[0][0]
        f = open(music_path,'rb')
        music_data = f.read()
        new_socket.send(music_data)



def main():
    ser_socket = socket(AF_INET,SOCK_STREAM)
    ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR , 1)
    ser_addr = ('192.168.14.153',5268)
    ser_socket.bind(ser_addr)
    ser_socket.listen(5)
    try:
        while True:
            new_socket,new_addr = ser_socket.accept()
            t = Thread(target=new_thread,args=(new_socket,new_addr))
            t.start()
    finally:
        ser_socket.close()

if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', user='root', password='0913', db='date20200115', charset='utf8')
    cur = conn.cursor()
    main()

