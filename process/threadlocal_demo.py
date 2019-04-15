# 一个ThreadLocal变量虽然是全局变量，
# 但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

import threading

# 创建全局ThreadLocal对象
local_student = threading.local()

class Student():
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def __str__(self):
		return "Name:" + self.name.ljust(6) + ' ' + "Age: " + str(self.age)


def process_student():
	std = local_student.student
	print(std,threading.current_thread().name)


def process_thread(std):
	local_student.student = std
	process_student()


std1 = Student("Tom",23)
std2 = Student("Jerry",25)

t1 = threading.Thread(target=process_thread,args=(std1,),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=(std2,),name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()