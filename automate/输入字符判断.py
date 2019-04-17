while True:
	age = input('Please enter your age :')
	if age.isdecimal():#字符串只包含数字，且非空
		print('Your age is :' , age)
		break
	print("Please enter a number for your age.")

while True:
	print('Select a new password (letters and numbers only):')
	password = input()
	if password.isalnum():#字符串只包含数字和字母，且非空
		print('Your password is '+ '\'' +password+'\'')
		break
	print('Passwords can only have letters and numbers.')		