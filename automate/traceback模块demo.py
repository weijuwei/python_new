import traceback

#traceback.format_exc()得到异常信息

def  spam():
	bacon()
def bacon():
	raise Exception('This is the error message!!!')

try:
	spam()
except:
	with open('D:\\桌面\\error.txt','w') as f:
		f.write(traceback.format_exc())