import threading,time

s = threading.Semaphore(2)

class My_thread(threading.Thread):
	def __init__(self,name):
		super(My_thread,self).__init__()
		self.name = name

	def run(self):
		s.acquire()
		print(threading.current_thread().name + '------> 我是' + self.name)
		time.sleep(1)
		print(self.name + '准备释放信号\n')
		print('当前信号为%d\n' %s._value)
		s.release()


# print(s._value)

list1 = ['张三','李四','王五','赵大','钱二','孙六','周七']
for i in range(7):
	t = My_thread(list1[i])
	t.start()