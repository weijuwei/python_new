# python3中广度优先继承
class A:
	def test(self):
		print('A')

class B(A):
	# def test(self):
	# 	print('B')
	pass

class C(A):
# 	def test(self):
# 		print('C')
	pass

class D(B):
	def test(self):
		print('D')


class E(C,D):
	pass

e = E()
e.test()
print(E.__mro__)  # mro列表基类的线性顺序列表 元组类型