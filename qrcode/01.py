import os,time
from PyPDF2 import PdfReader
# pip install pypdf2
# pip install Spire.PDF


save_dir = "png"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
 
# 提取图片
def exactImage(pdf_path):
    # 读取PDF文件
    pdf_reader = PdfReader(pdf_path)
    page = pdf_reader.pages[0]
    # print (page.images)
    image_nums = len(page.images) # 含有图片数量

    count = 0

    image_save_name_suffix = "" # 图片保存命名后缀编号

    if image_nums == 0:
        print("文件中不包含图片文件")
    else:
        print(f'{os.path.basename(pdf_path)}中包含共{image_nums}张图片')
        print('-' *20)
        for img_file_obj in page.images:

            if image_nums > 1:  
                image_save_name_suffix = "_" + str(count + 1)
                count += 1
            else:
                count = 1   
            
            # 图片保存路径
            image_save_dir = os.path.join(save_dir, f'{os.path.basename(pdf_path).split(".")[0]}{ image_save_name_suffix }.png')

            with open(image_save_dir, 'wb') as f:
                f.write(img_file_obj.data)
            # time.sleep(0.1)
            print(f'正在提取第{count}张图片')
        print('-' *20)
        print(f"{os.path.basename(pdf_path)}提取完成")
        print("#" * 25)
    # time.sleep(0.1)   


# from spire.pdf import *
# from spire.pdf.common import *
# 提取图片2
# def exactImage2(pdf):
#     pdf_doc = PdfDocument()
#     pdf_doc.LoadFromFile(pdf)
    
#     images = []
#     pdf_name = str(pdf).split(".")[0]

#     for i in range(pdf_doc.Pages.Count):
#         page = pdf_doc.Pages.get_Item(i)
#         for img in page.ExtractImages():
#             images.append(img)

#     for image in images:
#         image.Save(os.path.join(save_dir, f"{pdf_name}.png"))

def pdf_list(pdfs_dir):
    
    pdf_list = [] 
    if os.path.exists(pdfs_dir):
        for file in os.listdir(pdfs_dir):
            if '.pdf' in file:
                pdf_list.append(os.path.join(pdfs_dir, file))
        # print(pdf_list)
    else:
        print("目录不存在")
    return pdf_list

def main(pdf_list):
    if not pdf_list: 
        print("PDF列表为空！")
    else:
        for pdf in pdf_list:
            exactImage(pdf)
        print("\n\n所有文件提取成功\n\n")
        time.sleep(2)

pdf_list = pdf_list("pdfs")
# print(pdf_list)pdf_list

main(pdf_list)