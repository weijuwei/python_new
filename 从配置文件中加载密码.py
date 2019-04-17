# 从当前目录下加载mail.ini文件，并从中读取相关键值
import configparser,base64,os


def base64_str(b64_str):  # base64编码格式转换回string格式
	b = base64.b64decode(b64_str)
	return str(b,encoding='utf-8').strip()


config = configparser.ConfigParser()

if not os.path.isfile('mail.ini'):  # 没有指定文件，程序终止
	print("找不到mail.ini文件，程序终止。。。。")
	os._exit(0)

config.read('mail.ini')

from_addr = config.get('mail','from_addr')
to_addr = config.get('mail','to_addr')
password = config.get('mail','password')

print(from_addr)
print(to_addr)
print(password)

print('-'*20)

from_addr = base64_str(config.get('mail_base64','from_addr'))
to_addr = base64_str(config.get('mail_base64','to_addr'))
password = base64_str(config.get('mail_base64','password'))

print(from_addr)
print(to_addr)
print(password)