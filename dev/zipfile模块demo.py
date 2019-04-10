import zipfile,os

os.chdir('D:\\shutil_test')
'''
#Class with methods to open, read, write, close, list zip files.
zf = zipfile.ZipFile('test.zip') #读取test.zip文件
names = zf.namelist() #读取里面的文件名 返回一个list
print(names)

file_info = zf.getinfo('sleep.sh') #取得zip文件中指定的文件信息(namelist中含有的)
print(file_info.file_size) #文件大小
print(file_info.compress_size) #压缩后的大小

#解压缩
zf.extract("sleep.sh") #解压指定的文件到当前目录
zf.extractall()#解压所有文件到当前目录

zf.close()
'''
#创建压缩文件
newZip = zipfile.ZipFile('new.zip','w')#创建实例对象 w表示写入

newZip.write('sleep.sh',compress_type=zipfile.ZIP_DEFLATED)#添加文件，指定压缩类型
newZip.close()

#追加文件
newZip = zipfile.ZipFile('new.zip','a')# a表示追加文件
newZip.write('test1.py',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
