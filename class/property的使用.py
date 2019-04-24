class Room:
	def __init__(self,name,master,width,length):
		self.name = name
		self.master = master
		self.width = width
		self.length = length

	@property
	def area(self):
		return self.width * self.length

r1 = Room('bedroom','Tom',10,8)

# area = r1.area()  # error
area = r1.area

print('%s的%s面积是%d' %(r1.master,r1.name,area))