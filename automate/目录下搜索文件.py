import re,os

os.chdir('D:\\Desktop\\python')#切换目录

p = re.compile(r'模块') #匹配条件

files = [] #存放列表

for dp,dns,fns in os.walk('.'):#遍历整个目录下的所有文件
	for filename in fns:
		if p.search(filename):
			files.append(os.path.join(dp,filename))
			#files.append(filename)

for f in files:
	print(f)