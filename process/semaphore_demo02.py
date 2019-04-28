import threading,time

# 先对x进行赋值set操作，然后执行get操作

s = threading.Semaphore(0)  # 信号量初始化为0

x = 0  # 全局变量

def set_val(value):
	global 	x 
	x = value
	print('set thread ----> ' + str(x))
	print(threading.current_thread().name + 'release Semaphore')
	time.sleep(2)
	s.release()  # 信号量V操作 +1

def get_val():
	s.acquire()  # 信号量P操作 -1
	print('get thread ----> ' + str(x+1))


t_get = threading.Thread(target=get_val,args=())  # get线程获取操作

t_set = threading.Thread(target=set_val,args=(2,))  # set操作线程

t_set.start()
t_get.start()