import struct
from socket import *
filename = input('请输入要下载的文件名：')
server_ip = '192.168.14.25'
send_data = struct.pack('!H%dsb5sb'%len(filename),1,filename.encode(),0,'octet'.encode(),0)
s = socket(AF_INET,SOCK_DGRAM)
s.sendto(send_data,(server_ip,69)) #第一次发送，连接服务器69端口
f = open(filename,'ab') #以追加模式打开
while True:
    recv_data = s.recvfrom(600)
    caozuoma,ack_num = struct.unpack('!HH',recv_data[0][:4]) #获取数据块编号
    rand_port = recv_data[1][1] #获取服务器的随机端口
    print(recv_data)
    if int(caozuoma) == 5:
        print('文件不存在')
        break
    print('操作码：%d,ACK:%d,服务器随机端口：%d，数据长度：%d'%(caozuoma,ack_num,rand_port,len(recv_data[0])))
    f.write(recv_data[0][4:])
    if len(recv_data[0]) < 516:
        break
    ack_data = struct.pack('!HH',4,ack_num)
    s.sendto(ack_data,(server_ip,rand_port)) #回复ACK确认包

# import struct,os
# from socket import *
# file_name = input('请输入要下载的文件名(带后缀名)：')
# server_ip = '192.168.14.25'
# send_data = struct.pack('!H%dsb5sb'%len(file_name),1,file_name.encode(),0,'octet'.encode(),0)
# s = socket(AF_INET,SOCK_DGRAM)
# s.sendto(send_data,(server_ip,69))
# f = open(file_name,'ab')
# while True:
#     recv_data = s.recvfrom(1024)
#     caozuoma,ack_num = struct.unpack('!HH',recv_data[0][:4])
#     rand_port = recv_data[1][1]
#     if int(caozuoma) == 5:
#         print('找不到文件')
#         f.close()
#         os.remove(file_name)
#         break
#
#     print('操作码：{},ACK:{},服务器随机端口：{}，数据长度：{}'.format(caozuoma,ack_num,rand_port,len(recv_data[0])))
#     f.write(recv_data[0][4:])
#     if len(recv_data[0]) < 516:
#         print('传输完成')
#         break
#     ack_data = struct.pack('!HH',4,ack_num)
#     s.sendto(ack_data,(server_ip,rand_port))

# from multiprocessing import Queue,Process
# import time
#
# def write(q):
#     for value in ['a','b','c']:
#         print('开始写入：',value)
#         q.put(value)
#         time.sleep(1)
#
#
# def read(q):
#     while True:
#         if not q.empty():
#             print('读取到的是：',q.get())
#             time.sleep(1)
#         else:
#             break
#
# if __name__  == '__main__':
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pw.join() #等待接收完毕
#     pr.start()
#     pr.join()
#     print('接收完毕')

# from multiprocessing import Manager,Pool
# import time
#
#
# def write(q):
#     for i in 'welcome':
#         print('开始写入',i)
#         q.put(i)
#
# def reader(q):
#     time.sleep(3)
#     for i in range(q.qsize()):
#         print('得到消息',q.get())
#
# if __name__ == '__main__':
#     print('主进程启动')
#     q = Manager().Queue()
#     po = Pool()
#     po.apply_async(write, (q,))
#     po.apply_async(reader, (q,))
#     po.close()
#     po.join()


# import threading
# if __name__ == '__main__':
#     #任何进程默认会启动一个线程，这个线程称为主线程，主线程可以启动新的子线程
#     #current_thread():范围当前线程的实例
#     #.name：当前线程的名称
#     print('主线程%s启动'%(threading.current_thread().name))

# import threading,time
#
# def saySorry():
#     print('子线程程%s启动'%(threading.current_thread().name))
#     time.sleep(1)
#     print('亲爱的，我错了，我能吃饭了吗？')
#
# if __name__ == '__main__':
#     print('主进程%s启动'%(threading.current_thread().name))
#     for i in range(5):
#         t = threading.Thread(target=saySorry)
#         t.start()

# import threading
# import time
#
# def sing():
#     for i in range(3):
#         print('正在唱歌。。。%d'%i)
#         time.sleep(1)
#
# def dangce():
#     for i in range(2):
#         print('正在跳舞。。。%d'%i)
#         time.sleep(1)
#
# if __name__ == '__main__':
#     print('开始：%s'%time.time())
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dangce)
#     t1.start()
#     t2.start()
#
#     while True:
#         length = len(threading.enumerate())
#         # threading.unumerate(): 返回当前运行中的Thread对象列表
#         print('当前线程数为：%d'%length)
#         if length <= 1:
#             break
#         time.sleep(1)