from spire.pdf import *
from spire.pdf.common import *
import os
# pip install Spire.PDF


save_path = "png"
if not os.path.exists(save_path):
    os.mkdir(save_path)
    
    
# 提取图片
def exactImage(pdf):
    pdf_doc = PdfDocument()
    pdf_doc.LoadFromFile(pdf)
    
    images = []
    pdf_name = str(pdf).split(".")[0]

    for i in range(pdf_doc.Pages.Count):
        page = pdf_doc.Pages.get_Item(i)
        for img in page.ExtractImages():
            images.append(img)

    for image in images:
        image.Save(os.path.join(save_path, f"{pdf_name}.png"))
pdfs = []
for file in os.listdir():
    if '.pdf' in file:
        pdfs.append(file)

for pdf in pdfs:
    exactImage(pdf)

print("生成成功！！！")


# 生成txt文件


