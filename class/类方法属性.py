# 类对象可以直接调用类属性，也可以直接调用类方法
# 但不允许调用实例属性，并且也不允许调用实例方法
# 实例对象可以获取实例属性和类属性的值，调用实例方法和类方法，但不能修改类属性

class Students:
	__stu_nums = 0 # 类属性 伪私有  此处用作统计实例化的数量

	def __init__(self,name,age):  # 实例方法 
		self.name = name  # 实例属性
		self.age = age
		self.set_stu_nums()  # 每实例化一个对象 调用类方法

	def __str__(self):
		return self.name+' '+ str(self.age)

	@classmethod  # 类方法 @classmethod 装饰器
	def set_stu_nums(cls): # 类方法
		cls.__stu_nums += 1

	def get_stu_nums(self):
		return self.__stu_nums

	@classmethod
	def get_stu_instance(cls,stu_str):  # 通过字符串,返回一个对象实例
		name,age = stu_str.split('-')
		age = int(age)
		return cls(name,age)


stu1 = Students("Tom".ljust(6," "),23)  # ljust()左对齐
print(stu1)
stu2 = Students("Jerry".ljust(6," "),25)
print(stu2)
stu3 = Students("Bob".ljust(6," "),28)
print(stu3)
print(stu1.get_stu_nums())
stu_str = 'Lucy-22'
stu4 = Students.get_stu_instance(stu_str)
print(stu4)