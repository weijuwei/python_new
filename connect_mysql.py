import mysql.connector
# 先安装mysql-connector模块
# pip install mysql-connector

# HOST = '192.168.56.3'
# USER = 'root'
# PASSWORD = '123456'
# DATABASE = 'hellodb'
query = 'select name,age from students'
delete = "delete from students where name = '%s'" %(r'Yu Yutong')
update = "update students set gender = '%s' where name = '%s'" %('F',r'Guo Furong')
insert = "insert students(name,age,gender) values ('%s',%d,'%s')"%(r'Guo Furong',23,'M')

config = {  # 定义一个字典存放数据库连接信息 
		'host':'192.168.56.3',
		'user':'root',
		'password':'123456',
		'database':'hellodb'
	}

class mysql_cursor(object):  
	def __init__(self,**cconfig):
		self.conn = mysql.connector.connect(**config)
		self.cursor = self.conn.cursor()

	def exec(self,sql):  # 简单地插入、更新、删除操作
		try:
			self.cursor.execute(sql)
			self.conn.commit()  # 事务提交
		except:
			print("操作失败！！！")
			self.rollback()  # 事务回滚
		finally:
			self.conn.close()

	def query(self,sql):  # 简单查询操作
		self.cursor.execute(sql)
		# values = self.cursor.fetchall()
		# return values  # 返回查询结果
		return self.cursor

	def conn_close(self):
		self.conn.close()

my_cursor = mysql_cursor(**config)
values = my_cursor.query(query)

for i in values:
	print(i)

my_cursor.conn_close()

# 创建mysql连接对象
# conn = mysql.connector.connect(host=HOST,user=USER,password=PASSWORD,database=DATABASE)
# conn = mysql.connector.connect(**config)  # 通过传入字典，创建mysql连接对象

# cursor = conn.cursor()  # 实例化一个cursor

'''
# 查询操作
# cursor.execute(query)
# # stds = cursor.fetchall()  #一次性取得所有查询数据，占用内存 
# for row in cursor:
# 	print(row[0].ljust(13),str(row[1]).rjust(4))

# 删除数据条目操作
# try:
# 	cursor.execute(delete)
# 	conn.commit()
# except:
# 	print("删除操作失败！")
# 	conn.rollback()

# 更新数据条目操作
# try:
# 	cursor.execute(update)
# 	conn.commit()
# except:
# 	print("更新操作失败！")
# 	conn.rollback()

# 插入数据条目操作
try:
	cursor.execute(insert)
	conn.commit()
except:
	print("插入数据失败！")
	conn.rollback()

cursor.close()
conn.close()  # 关闭数据库连接
'''