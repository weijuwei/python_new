import qrcode
from PIL import Image, ImageDraw, ImageFont

# 输入要生成的文本信息
data = "Hello, QR Code!"

# 创建 QR 码对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)
qr.add_data(data)
qr.make(fit=True)

# # 获取 QR 码的内容
# qr_content = qr.make_image(fill_color="black", back_color="white").get_data()

# 创建 QR 码图片
qr_img = qr.make_image(fill_color="black", back_color="white")

w,h = qr_img.size
print(w,h)

bg = Image.new("RGB",(w, h+20), "#ffffff")

bg.paste(qr_img, (0, 0))

# 在 QR 码图片下方添加文字
draw = ImageDraw.Draw(bg)
font = ImageFont.load_default()  # 使用默认字体，也可以指定其他字体

text_width, text_height = draw.textsize(data, font)
print(text_width, text_height)

text_position = ((w - text_width) / 2, h)
draw.text(text_position, data, fill="black", font=font)

# 保存 QR 码图片
# qr_img.save("my_qrcode_with_text.png")
bg.show()