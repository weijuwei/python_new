import time

class FileHandler:
	def __init__(self,filename,mode='r',encoding='utf-8'):
		self.file = open(filename,mode,encoding='utf-8')
		self.mode = mode
		self.encoding = encoding

	def __getattr__(self,item):
		# print(item)
		# print('%s property not found......' %item)
		return getattr(self.file,item)

	def write(self,content):
		t = time.strftime('%Y-%m-%d %X')
		self.file.write(t+ ' ' +content)

f1 = FileHandler('test.txt','w+',encoding='utf-8')

f1.write('ssssssssssssssssssss\n')

f1.seek(0)
print(f1.read())