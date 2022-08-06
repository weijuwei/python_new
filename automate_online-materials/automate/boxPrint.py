#boxPrint() 函数，它接受一个字符、一个宽度和一个高度。它
#按照指定的宽度和高度，用该字符创建了一个小盒子的图像
def boxPrint(symbol,width,height):
	if len(symbol) != 1:
		raise Exception('Symbol must be a single character string.')
	if width <= 2:
		raise Exception('Width must be greater than 2.')
	if height <= 2:
		raise Exception('Height must be greater than 2.')

	print(symbol * width)	

	for i in range(height - 2):
		print(symbol + (' ' * (width - 2) + symbol))
	print(symbol * width)

for sym,w,h in(('*',5,3),('+',5,3),('-',10,6)):
	try:
		boxPrint(sym,w,h)
	except Exception as e:
		print('error')