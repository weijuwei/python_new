import time,logging

def timer(func):
	def wrapper():
		start_time = time.time()
		logging.warning("start time")
		func()
		stop_time = time.time()
		print(func.__name__+"运行时间： " ,(stop_time - start_time))
		logging.warning("stop time")
	return wrapper	
@timer
def test():
	time.sleep(3)
	#print("test运行OK")

#test = timer(test)
test()	
