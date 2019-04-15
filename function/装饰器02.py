import time,logging

def timer(func):
	def wrapper():
		start_time = time.time()
		logging.warning("start time")
		ret = func()
		stop_time = time.time()
		logging.warning("stop time")
		print(func.__name__+"运行时间： " ,(stop_time - start_time))
		return ret
	return wrapper	
@timer
def test():
	time.sleep(3)

	return "test中的值"
	#print("test运行OK")

#test = timer(test)
resp = test()	
print(resp)