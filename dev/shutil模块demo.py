import shutil,os,send2trash
#Utility functions for copying and archiving files and directory trees.
#send2trash move file or directory to the trash

workDir = 'd:\\shutil_test'

if not os.path.exists(workDir):
	os.makedirs(workDir)

os.chdir(workDir)#路径切换到workDir目录

absDir = os.path.abspath('.') #当前位置绝对路径
print("当前位置绝对路径是：",absDir)

# shutil.copy('d:\\test.py','.') #copy d:\test.py到当前目录
# print(os.listdir()) #列出当前目录的文件 返回类型为list
# shutil.copy('test.py','test_cp.py') #复制test.py文件为test_cp.py
# shutil.copytree('d:\\shutil_test','d:\\shutil_test_backup') # 复制文件夹操作
# shutil.move('test.py','test_move.py') #重命名操作 在同一路径下
# shutil.move("test_move.py",'d:\\') #移动文件操作，移动到指定dest下
# os.unlink('test.py') # 删除文件操作
# os.rmdir('ss') #删除文件夹操作
# shutil.rmtree('ss')#删除文件夹以及文件夹下的所有文件.文件不可恢复
for filename in os.listdir():
	if filename.endswith('.py'):
		print(filename)
send2trash.send2trash('test_cp.py')#将文件删除到回收站里 ，可以轻易地手动恢复
print(os.path.isfile("test_cp.py"))#判断是否删除