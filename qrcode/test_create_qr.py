from PIL import ImageFont, ImageDraw, Image
import qrcode

text = "GATP00000001 GATP00000050"
text1 = "GATP00000001\nGATP00000050"

qr = qrcode.QRCode( 
       version=4,
       error_correction=qrcode.constants.ERROR_CORRECT_H,
       # 比例大约等于1:28
       box_size=10,
       border=1,
    )

qr.add_data(text)
qr.make(fit=True)
qr_img = qr.make_image(fill_color='black', back_color='white')

# qr_img.show()

w, h = qr_img.size
print(w,h)

bg = Image.new("RGB", (w, h + 50), "#ffffff")
bg.paste(qr_img, (0, 0))
# bg.show()

draw = ImageDraw.Draw(bg)

font = ImageFont.truetype(font="arial.ttf", size=20)
# text_w, text_h = draw.textsize(text1, font)
i, j, k, l = font.getbbox(text1)
print(i, j, k, l)

# bg_new = Image.new("RGB", (int(k/2), (l+j)*2), "#ffffff")
# draw1 = ImageDraw.Draw(bg_new)
# draw1.text((0,0), text1,fill="black",font=font)

# bg_new.show()


# draw.text(((w - text_w)/2, h), text1, fill="black", font=font)
draw.text(((w - k/2)/2, h), text1, fill="black", font=font)



# print(bg.size)

# bg.save("11.png")
bg.show()