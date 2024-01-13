import qrcode
from PIL import Image, ImageDraw, ImageFont

# 输入要生成的文本信息
# data = "Hello, QR Code!"

data="GATP00000001\rGATP00000002\rGATP00000003\rGATP00000004\rGATP00000005\rGATP00000006\rGATP00000007\rGATP00000008\rGATP00000009\rGATP00000010\rGATP00000011\rGATP00000012\rGATP00000013\rGATP00000014\rGATP00000015\rGATP00000016\rGATP00000017\rGATP00000018\rGATP00000019\rGATP00000020\rGATP00000021\rGATP00000022\rGATP00000023\rGATP00000024\rGATP00000025\rGATP00000026\rGATP00000027\rGATP00000028\rGATP00000029\rGATP00000030\rGATP00000031\rGATP00000032\rGATP00000033\rGATP00000034\rGATP00000035\rGATP00000036\rGATP00000037\rGATP00000038\rGATP00000039\rGATP00000040\rGATP00000041\rGATP00000042\rGATP00000043\rGATP00000044\rGATP00000045\rGATP00000046\rGATP00000047\rGATP00000048\rGATP00000049\rGATP00000050\r"

# 创建 QR 码对象
qr = qrcode.QRCode(
    version=4,
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
qr_img.save("111.png")
# bg.show()