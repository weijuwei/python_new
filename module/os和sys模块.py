import sys,os


print(sys.argv)  # 获取命令行参数，list类型，第一个是程序本身
print(sys.version)  # 获取当前python解释程序的版本信息
print(sys.platform)  # 获取当前操作系统平台名称
print(len(sys.argv))  # 获取参数个数

print(os.name)
print(os.sep)
# print(os.environ)

print(os.stat('config.ini'))  # 获取文件元数据信息
# os.removedirs('os_test\\test2')  # 递归删除目录，目录为空则无法删除，并报错

print(os.getcwd())  # 获取当前目录
# os.mkdir('os_test')  # 创建一个目录 
# os.rmdir('os_test')  # 删除一个目录
# os.rename('os_test','os_test1')  # 修改文件名字

# os.chdir('os_test')  # 改变目录
# print(os.listdir())  # 列出目录下的内容 list类型

print(os.path.exists('os_test')) # 判断路径是否存在
print(os.path.isabs('os_test'))  # 判断是否是绝对路径
# tree_dir = os.walk('.')  # 目录树生成

# for dp,dn,fn in tree_dir:
# 	for f in fn:
# 		print(os.path.join(dp,f))  # 路径组合

print(os.path.split('os_test\\s'))  # 分割成目录和文件名二元组
print(os.path.dirname('os_test\\s'))  # 返回目录名
print(os.path.basename('os_test\\s'))  # 返回路径基名

print(os.path.getatime('os_test\\s'))  # 返回指定文件或目录最后的存取时间
print(os.path.getmtime('os_test\\s'))  # 返回最后修改时间