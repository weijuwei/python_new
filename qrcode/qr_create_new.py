from PIL import ImageFont, ImageDraw, Image
import qrcode
import os,time

# 根据指定文本内容创建二维码
def createQrCode(text):
  # 二维码尺寸规格
  qr = qrcode.QRCode( 
       version=4,
       error_correction=qrcode.constants.ERROR_CORRECT_H,
       # 比例大约等于1:28
       box_size=20,
       border=2,
    )
  qr.add_data(text) # 文本内容
  qr.make(fit=True)
  qr = qr.make_image(fill_color="black", back_color="white")
  return qr

# 新建背景图合并二维码图片和显示文字
def createBg(qrImg,qrText):
  
  # 二维码图片尺寸
  w, h = qrImg.size

  # 新建背景图尺寸
  bg_w = w
  bg_h = h + 90
  bg = Image.new("RGB", (bg_w, bg_h), "#ffffff")

  # 将二维码图片添加的新的背景图里面
  bg.paste(qrImg, (0, 0))

  # 创建二维码下面显示文字
  font_size = 30 # 字体大小
  font = ImageFont.truetype("arial.ttf",size=font_size)
  
  words_img = ImageDraw.Draw(bg) 
  
  # 获取文本size
  text_w, text_h = words_img.textsize(qrText, font)
  
  # 文本位置
  text_position = ((bg_w - text_w) / 2, h)
  
  # print(text_position)
  
  # 将文本添加到图片中
  words_img.text(text_position, qrText, fill="#000000", font=font)

  # bg.show()
 
  return bg # 返回最终生成的图片

# qr_text = "GATP00000001\nGATP00000050"

# qr = createQrCode(qr_text)
# createBg(qr, qr_text)


# 保存二维码图片目录
save_path = "qrcodes"
if not os.path.exists(save_path):
  os.mkdir(save_path)

# 根据对应text文本文件内容创建二维码图片
with open("qrcode.txt", 'r') as f:
  lines = f.readlines()
  for line in lines:
    texts = line.strip().split(' ')
    qr_text = texts[0] + '\n' + texts[1]
    qr = createQrCode(qr_text)
    bg = createBg(qr, qr_text)
    bg.save(os.path.join(save_path,f"{texts[0][-8:]}.jpg")) # 输出到指定目录

print("----------------创建成功------------------")   
time.sleep(3)