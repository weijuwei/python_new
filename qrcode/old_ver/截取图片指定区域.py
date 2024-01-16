import cv2
from pyzbar.pyzbar import decode
from PIL import Image

def identify_qrcode(img_path):
	img = cv2.imread(img_path)

	# 转换成灰度图像
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# 识别二维码
	decoded = decode(gray)

	# 打印内容
	for d in decoded:
		print(d.data.decode())

	for obj in decoded:
		rect = obj.rect
		cv2.rectangle(img, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height),(0, 255, 0), 2)

	# cv2.imshow("Result", img)
	cv2.imshow("ROI", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return decoded



contents = identify_qrcode("png\\1-1.png")

"""
left 左上角距离图片左边界距离
top  左上角距离图片上边界距离
width 二维码宽度
height 二维码高度
lef + width 右下角距离图片左边界距离
top + height 右下角距离图片上边界距离
"""
left, top, width, height = contents[0][2]

print(left, top, width, height)
print(type(left))

qr_code_postion = (left, top, left + width, top + height)

img = Image.open("png\\1-1.png")
box = (210, 22, 388, 200)

roi = img.crop(qr_code_postion)
roi.save("11111.png")

# for i in contents[0][2]:
# 	print(i)