import cv2
from pyzbar.pyzbar import decode

def identify_qrcode(img_path):
	img = cv2.imread(img_path)

	# 转换成灰度图像
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# 识别二维码
	qr_decoded = decode(gray)

	content = qr_decoded[0][0].decode()
	# print(content.split())
	# print(decoded)
	return content.split()
	# # 打印内容
	# for d in decoded:
	# 	print(d.data.decode())

	# for obj in decoded:
	# 	rect = obj.rect
	# 	cv2.rectangle(img, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height),(0, 255, 0), 2)

	# cv2.imshow("Result", img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()


h = identify_qrcode(r"png\1-1.png")
print(h[0],h[-1])