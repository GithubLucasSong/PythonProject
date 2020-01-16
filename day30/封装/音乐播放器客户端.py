from socket import *
import pygame
import time

s = socket(AF_INET,SOCK_STREAM)
ser_addr = ('192.168.14.153',5268)
s.connect(ser_addr)
redata = s.recv(1024)
if len(redata):
    print(redata.decode())
data = input()
s.send(data.encode())
while True:
    redata = s.recv(1024)
    if len(redata) > 0:
        with open(f'{data}.mp3','ab') as f:
            f.write(redata)
        if len(redata)<1024:
            break

pygame.mixer.init()
pygame.mixer.music.load(f'{data}.mp3')
pygame.mixer_music.play()
print('音乐开始播放')
time.sleep(500)



