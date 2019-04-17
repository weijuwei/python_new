#!/usr/bin/python3
# 参考： https://blog.csdn.net/u013066730/article/details/73457463
import os
import subprocess


# os.system('command') 只在终端运行系统命令，而不能获取命令执行的返回结果
# 只是将执行结果输出到当前终端中 返回状态码
os.system('ifconfig enp0s3')

# popen()函数 可以获取执行的返回结果，保存在list中
# 将结果保存到定义的变量中，便于程序后续处理
list1 = os.popen('tail -n5 /var/log/messages').readlines()
print(list1)

# os.poen(command,mode)
# 打开一个与command进程之间的管道。这个函数的返回值是一个文件对象，
# 可以读或者写(由mode决定，mode默认是’r')。如果mode为’r'，
# 可以使用此函数的返回值调用read()来获取command命令的执行结果。
result = os.popen("ifconfig" ,'r')
r = result.read() 将读取结果保存到一个变量中

# 使用subprocess模块
subprocess.call('ls')
subprocess.Popen('ls')
# 将shell command执行状态保存到handle变量中  相当于linux中执行完command后 echo $?
handle = subprocess.call('ls -l',shell=True)

# 将shell command执行结果保存到变量中
handle = subprocess.Popen('date',shell=True,stdout=subprocess.PIPE)
handle.stdout.read()  #读取执行结果
