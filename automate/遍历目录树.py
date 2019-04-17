import os

#os.walk()  dirpath, dirnames, filenames
#返回3个值 
#	当前文件夹名称的字符串 
#	当前文件夹中子文件夹的字符串列表
#	当前文件夹中文件的字符串的列表 
 
for dirpath,dirnames,filenames in os.walk('D:\\Downloads\\nexus5x'):
	print('当前文件夹是：' + dirpath)
	for dirname in dirnames:
		print(dirpath + '的子文件夹: ' + dirname)

	for filename in filenames:
		print(dirpath+'下包含：'+filename)