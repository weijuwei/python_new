class Person:
	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender

	def __delattr__(self,name):  # 对象方法，删除实例对象是调用
		print('__delattr__ running....')

	def __setattr__(self,key,value):  # 对象方法，设置实例属性时调用
		print('__setattr__ running')
		self.__dict__[key] = value

	def __getattr__(self,key):  # 对象方法，访问属性失败时调用
		print("__getattr__ running ,property %s not found" %key)

p1 = Person('Tom',23,'M')
print(hasattr(p1,'name'))

setattr(p1,'age',34)  # 设置属性
print(p1.age)
print(getattr(p1,'name2','none_name2'))  # 取得属性,没有，则返回默认值
print(getattr(p1,'name'))

print(p1.__dict__)

delattr(p1,'gender')  # 删除属性

print(p1.__dict__)

setattr(p1,'func',lambda x:x+1)  # 设置匿名函数
print(p1.func(5))