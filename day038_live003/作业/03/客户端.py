from socket import *
socket = socket(AF_INET,SOCK_STREAM)
addr = ('',8888)
socket.bind(addr)
seraddr = ('192.168.1.7',7777)
socket.connect(seraddr)
socket.send('你好'.encode('utf-8'))