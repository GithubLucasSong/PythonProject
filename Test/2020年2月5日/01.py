import threading
num = 0
def test1():
    global num
    for i in range(1000000):
        if mutex.acquire():
            print('线程1')
            num += 1
            mutex.release()
def test2():
    global num
    for i in range(1000000):
        if mutex.acquire():
            print('线程2')
            num += 1
            mutex.release()

mutex = threading.Lock()
p1 = threading.Thread(target=test1)
p2 = threading.Thread(target=test2)
p1.start()
p2.start()
p1.join()
p2.join()
print(num)
