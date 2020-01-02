from socket import *
udpSocket = socket(AF_INET,SOCK_DGRAM)
binAddr = ('',8887)
udpSocket.bind(binAddr)
recvData = udpSocket.recvfrom(1024)
print(recvData)

