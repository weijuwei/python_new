#!/usr/bin/python3
import os
import subprocess
# https://blog.csdn.net/u013066730/article/details/73457463

# os.system('command') 只在终端运行系统命令，而不能获取命令执行的返回结果
# 只是将执行结果输出到当前终端中
os.system('ifconfig enp0s3')

# popen()函数 可以获取执行的返回结果，保存在list中
# 将结果保存到定义的变量中，便于程序后续处理
list1 = os.popen('tail -n5 /var/log/messages').readlines()
print(list1)

# 使用subprocess模块
subprocess.call('ls')
subprocess.Popen('ls')
