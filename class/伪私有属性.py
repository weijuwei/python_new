# Python的伪私有属性，实际是通过变量名压缩（mangling）来实现变量名局部化。
# 变量名压缩的规则：在初始的变量名头部加上一个下划线，
# 再加上类的名称，最后是初始变量名的名称。
class Person:

	# nation = 'China'
	# _nation = 'China'
	__nation = 'China'

	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender

	def __info(self):
		print(self.name,self.age)

	def get_nation(self):  # 访问函数
		return self.__nation

	def set_nation(self,nation):
		self.__nation = nation


p1 = Person('Tom',23,'M')

# print(Person.__dict__)
# print('nation = %s' %p1.nation)
# print('_nation = %s' %p1._nation)
# print(p1.__nation)  # error
print('__nation = %s' %p1._Person__nation)

# p1.__info()   # error

p1._Person__info()

p1.set_nation('USA')

print(p1.get_nation())

