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
       border=1,
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
  bg_h = h + 80
  bg = Image.new("RGB", (bg_w, bg_h), "#ffffff")

  # 将二维码图片添加的新的背景图里面
  bg.paste(qrImg, (0, 0))

  # 创建二维码下面显示文字
  font_size = 30 # 字体大小
  font = ImageFont.truetype("arial.ttf",size=font_size)
  words_img = ImageDraw.Draw(bg)
  words_img.text((270,bg_w),qrText,fill="#000000",font=font)
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

# # print(qr.size[0])
# # qr.show()

# w, h = qrImg.size # 二维码wide high
# # print(w,h)
# bg_w = w # 背景画布wide
# bg_h = h + 60 # 背景画布high
# bg = Image.new("RGB", (bg_w, bg_h), "#ffffff")
# bg.paste(qrImg, (0, 0))

# font_size = 24
# font = ImageFont.truetype("arial.ttf",size=font_size)

# words_img = ImageDraw.Draw(bg)


# words_img.text((270,bg_w),qr_text,fill="#000000",font=font)
# bg.show()

# # 创建背景画布
# def createBg(qrImg):
#    img = qrImg.resize((580, 580))
#    bg = Image.new("RGB", (580, 650), "#ffffff")
#    bg.paste(img, (0, 0))
#    return bg

# # 添加二维码下面显示文字
# def drawFont(bg, text):
#    fontStyle = "arial.ttf"
#    font = ImageFont.truetype(fontStyle, 24)
   
#    draw = ImageDraw.Draw(bg)
#    draw.text((210, 580), text, fill="#000000", font=font)
#    return bg

# # 将二维码和显示文字添加到背景画布里面
# def draw(qrText, descText):
#    qrImg = createQrCode(qrText)
#    bgImg = createBg(qrImg)
#    bgImg2 = drawFont(bgImg, descText)
   
#    bgImg2.save(f"{qrText}.jpg")
#    # bgImg2.show()

# # draw("GATP00000001 GATP00000050","GATP00000001\nGATP00000050")

# """
# 参数说明: draw(qrText, descText)
# qrText: 二维码显示的内容
# descText: 二维码下面的文案显示
# """

# # 从qrcode.txt文件读取内容最终生成需要的二维码图片
# with open("qrcode.txt" ,'r', encoding="utf-8") as f:
#    lines = f.readlines()
#    for line in lines:
#       qr_text = line.strip()
#       texts = line.strip().split(' ')
#       desc_text = texts[0] + '\n' + texts[1]
#       draw(qr_text, desc_text)s