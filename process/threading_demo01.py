import time,threading


def exec_fun():
	print("线程 %s " %threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('线程 %s -> %d' %(threading.current_thread().name,n))
		time.sleep(1)
	print("线程 %s 结束。" %threading.current_thread().name)	


print("线程 %s 正在运行。"% threading.current_thread().name)  # 取得当前线程名

t = threading.Thread(target=exec_fun,name='SubThread')  #创建一个线程实例，并命名为SubThread
t.start()  # 启动线程
t.join()  # 等待直到线程结束