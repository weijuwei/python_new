import os,time
# import cv2
from pyzbar.pyzbar import decode
from PIL import Image
# pip install opencv-python
# pip install pyzbar

if not os.path.exists("qrcode"):
	os.mkdir("qrcode")

def capture_qrcode(image_path):

	# image = cv2.imread(image_path)
	# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	img = Image.open(image_path)
	qrcode_decode = decode(img)

	# 识别二维码内容(文本内容)，并处理成列表
	datas = qrcode_decode[0][0].decode()
	content = datas.split()

	file_name = content[0] + '_' + content[-1]

	"""
	left 左上角距离图片左边界距离
	top  左上角距离图片上边界距离
	width 二维码宽度
	height 二维码高度
	lef + width 右下角距离图片左边界距离
	top + height 右下角距离图片上边界距离
	"""
	left, top, width, height = qrcode_decode[0][2]
	# print(left, top, width, height)

	# 截取区域定位
	qrcode_postion = (left, top, left + width, top + height)

	img = Image.open(image_path)

	# 截取指定区域
	capture_qr = img.crop(qrcode_postion)

	# 保存截取内容
	save_path = os.path.join("qrcode",f'{os.path.basename(image_path).split(".")[0]}_{ file_name }.png')
	# print(save_path)

	capture_qr.save(save_path)

# capture_qrcode(r"png\1-1.png")

def main(png_dir):
	for png in os.listdir(png_dir):
		capture_qrcode(os.path.join("png", png))


main("png")
print("抓取二维码区域图片成功")