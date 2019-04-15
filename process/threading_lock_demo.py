# 如果我们要确保balance计算正确，就要给change_it()上一把锁，
# 当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，
# 因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。
# 由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，
# 所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现
import time,threading

balance = 0
lock = threading.Lock()  # 创建一个线程锁实例


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):  #线程执行体
    for i in range(200020):
        lock.acquire()  # 获取锁
        try:
            change_it(n)
        finally:
            lock.release()  # 释放锁


t1 = threading.Thread(target=run_thread,args=(5,))  # 创建线程实例
t2 = threading.Thread(target=run_thread,args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)