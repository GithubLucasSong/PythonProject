from socket import *
from multiprocessing import *


def func(new_s,new_addr):
    while True:
        recv = new_s.recv(1024)
        if len(recv)>0:
            print(recv)
        else:
            break
    new_s.close()

def main():
    s = socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    addr = (("",4567))
    s.bind(addr)
    s.listen(5)
    try:
        while True:
            new_s,new_addr = s.accept()
            p = Process(target=func,args=(new_s,new_addr))
            p.start()

if __name__ == '__main__':
    main()


import socketserver
class Myserver(socketserver.BaseRequestHandler):
    #必须写入handler方法，建立连接时会自动执行handle方法
    def handle(self):
        while True:
            data = self.request.recv(1024)
            print(data)

socketserver.TCPServer.allow_resue_address = True
server = socketserver.ThreadingTCPServer(('192.168.14.25',6789),Myserver)
server.serve_forever()
