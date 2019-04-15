import configparser

##https://docs.python.org/zh-cn/3/library/configparser.html

config = configparser.ConfigParser()
config.read('config.ini')

master_name = config.get('master','master_name')#取得指定sectiond中的指定option值
print(master_name)

# config.remove_section('section')#删除指定的section

#读取所有内容
def read_content():	
	sec = config.sections()##返回章节[] 类型是list Return a list of section names
	print(sec,type(sec))
	# master = config['master'] ##返回章节字典dict,可以对其遍历读取内容
	print("-----我是分割线-----")	
	for s in sec:
		se = config[s] #取得sections
		for key in se:   #对每个sections进行遍历读取
			print(key," = ",se[key])
		print("-----我是分割线-----")	

#更新数据
def modify_content(sec,key,value):
	print(config.sections())
	f = open('config.ini','w')
	#config[sec][key] = value
	config.set(sec, key, value)#更新指定sectiond中的指定option的value
	config.write(f)
	f.close()

#添加数据 取得sections 添加到指定sectiongs中
def insert_content(sec,key,value):
	f = open('config.ini','w')
	config[sec][key] = value
	config.write(f)
	f.close()

#删除数据
def remove_content(sec,key):
	f = open('config.ini','w')
	config.remove_option(sec,key)#删除指定sections中的指定键值
	config.write(f)
	f.close()