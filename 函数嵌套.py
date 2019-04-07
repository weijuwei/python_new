def base(name):
	print("base name :" ,name)
	def sub():
		name = 'sub'
		print("sub name : " ,name)
		def sub2():
			name = "sub2"
			print("sub2 name : " , name)
		sub2()
	sub()

base("base")