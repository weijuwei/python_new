import os,time

qrcode_pngs = os.listdir("qrcode")

png_save_path = r"D:\DESKTOP\GEMALTO\qrcode"

if os.path.exists("qrcode.txt"):
    os.remove("qrcode.txt")

txt_lines = []

for png in qrcode_pngs:
    png_name = os.path.splitext(png)[0].split("_")
    # print(png_name)
    txt_lines.append(f'{os.path.join(png_save_path, png)},{png_name[0]},{png_name[1]},{png_name[2]}')

with open('qrcode.txt','a', encoding="utf-8") as f:
    counter = 0
    f.write("图片路径,I/B,首编号,末编号\n")
    for line in txt_lines:
        if counter < len(txt_lines) - 1:
            f.write(line + "\n")
        else:
            f.write(line)
        counter += 1

print("============创建数据txt文件成功============")
time.sleep(5)