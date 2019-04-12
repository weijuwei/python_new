import logging

#日志级别 
# DEBUG 最低级别。用于小细节，通常只有在诊断问题时，才会关心这些消息
# INFO  用于记录程序中一般事件的信息，或确认一切工作正常
# WARNING 用于表示可能的问题，它不会阻止程序的工作，但可能会
# ERROR 用于记录错误，它导致程序做某事失败
# CRITICAL 最高级别。用于表示致命的错误，它导致或将要导致程序完全停止工作


# 定义要记录的日志级别、格式
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

# 将日志保存到指定文件当中
# logging.basicConfig(filename='logging.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

#logging.disable(logging.CRITICAL) #禁用日志 禁用之后的的日志信息，之前定义的无影响
def factorial(n):
	logging.debug('Start of factorial(%s)' %(n))
	total = 1
	for i in range(1,n+1):
		total *= i
		logging.debug('i is ' + str(i) + ', total is ' + str(total))
	logging.debug('End of factorial(%s)' %(n))
	return total 
print(factorial(7))	
logging.debug('End of program')