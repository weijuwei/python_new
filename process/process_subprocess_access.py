import time,random,os
from multiprocessing import Process,Queue


def write(queue,data):  # 写数据
    print('write pid :',os.getpid())
    for value in data:
        print("put %s to queue" %value)
        queue.put(value)
        time.sleep(random.random())


def read(queue): # 读数据
    print('read pid : ',os.getpid())
    while not queue.empty():
        value = queue.get(True)
        print("get %s from queue"%value)
        time.sleep(1)


if __name__ == '__main__':
    q = Queue()  # 创建队列

    print('main process pid :',os.getpid())

    data = ['A','B','C','D']

    pw = Process(target=write,args=(q,data,))  # 写进程
    pr = Process(target=read,args=(q,))  # 读进程

    pw.start()
    pr.start()

    pw.join()
    pr.join()
