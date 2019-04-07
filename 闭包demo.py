

def outer():
	list1 = []
	def inner():
		for i in range(10):
			list1.append(i)

		return list1
	return inner

res = outer()
ss = res()

print(ss)		