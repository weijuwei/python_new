from PIL import Image
import pytesseract


img = Image.open("1-1.png")

text = pytesseract.image_to_string(img)

# text = tool.image_to_string(img, lang="chi_sim", builder=pyocr.builders.TextBuilder())

print(text)
print("-" * 20)
txts = text.split()

print(txts)