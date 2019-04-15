
##模拟网站登陆浏览

# 用一个字典模拟session功能
user_dic = {"username": None,"login": None} 

##模拟网站登陆认证功能
def auth(func):
	def login(*args,**kwargs):
		# 判断user_dic是否为空 不为空则后续可以跳过再次认证
		if user_dic['username'] and user_dic['login']: 
			res = func(*args,**kwargs)
			return res

		# 模拟输入用户名和密码
		username = input("pls input username:").strip(); 
		passwd = input("pls input your password:").strip()

		# 对用户名和密码进行判断 正确则执行，并将状态信息写入user_dic中
		if username == 'weijuwei' and passwd == '123456':
			user_dic['username'] = username
			user_dic['login'] = True
			res = func(*args,**kwargs)
			return res
		else:			
			print('you uesername or password is wrong,pls input again !!!!')
			return False
	return login	

@auth
def home(): ##模拟进入用户主页 
	print("this is your home page..")

@auth
def cart():	##模拟用户购物车
	print("this is your cart")

@auth
def order(): ##模拟用户订单
	print("this is your order")		

home()
cart()
order()