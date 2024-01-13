import cv2
from pyzbar.pyzbar import decode

#pip install opencv-python
#pip install pyzbar


image = cv2.imread("111.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

barcodes = decode(gray)
print(type(barcodes))
print(barcodes[0][0].decode())

# for bar in barcodes:
# 	points = bar.polygon
# 	if len(points) == 4:
#         # pts = [(int(x), int(y)) for x, y in points]

#         # # 在图像上绘制边界框
#         # cv2.polylines(image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

#         # 提取二维码内容
#         barcode_data = barcode.data.decode("utf-8")
#         print("QR Code:", barcode_data)

# 显示带有二维码边界框的图像
# cv2.imshow("QR Code", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()