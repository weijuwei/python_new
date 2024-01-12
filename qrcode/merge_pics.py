from PIL import Image
import os,math,time,subprocess

# images_files = ['1.jpg', '2.jpg', '3.jpg', '4.jpg','11.jpg', '22.jpg', '33.jpg', '44.jpg']
if not os.path.exists("qrcodes"):
    print("没检测到目录！")

images_files = []
for f in os.listdir("qrcodes"):
   images_files.append(os.path.join("qrcodes",f))
# images_files = os.listdir("qrcodes")
count = len(images_files) # 目录包含图片数量
if count == 0:
    print("目录为空！")

# 获取单张二维码图片尺寸
img = Image.open(images_files[0])
w = img.size[0]
h = img.size[1]

# 创建合并后新的图片的尺寸
new_img_w = int(w * 4) # 宽度可容纳4张二维码图片
new_img_h = int(h * math.ceil( count / 4 )) # 列高根据图片数量向上取整

# print(new_img_h,new_img_w)
new_img = Image.new('RGB', (new_img_w, new_img_h), 'white')

# 创建N行4列
for i, f in enumerate(images_files):
    row = int(i/4)
    col = i%4
    # print(row,col)
    f = Image.open(f)
    new_img.paste(f, (col * w, row * h ))

# 输出到新的图片文件
new_img.save("out.jpg")

print("============合并图片成功=============")

time.sleep(3)

# 打开合并后的文件
# subprocess.call("start out.jpg", shell=True)