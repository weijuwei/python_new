# pw.py - insecure password locker program
# 当程序的参数是PASSWORDS中的key时，取得key对应的值复制到剪贴板中

PASSWORDS = {'email':'root',
			'blog':'admin',
			'qq':'123456'}

import sys,pyperclip

if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1] #第一个命令行参数是account name
if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)