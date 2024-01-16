import os,time
from PyPDF2 import PdfReader
# pip install pypdf2

pdf_path = r"6_8.pdf"

save_dir = "png" # 图片保存目录
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

# pdf_file = open('1-1.pdf', 'rb')
# pdf_reader = PyPDF2.PdfReader(pdf_file)

# 读取PDF文件
pdf_reader = PdfReader(pdf_path)
print(f'{ os.path.basename(pdf_path) }文件共{ len(pdf_reader.pages) }页')

pages = pdf_reader.pages

image_save_name_suffix = "" # 图片保存命名后缀编号
page_num = 1

for page in pages:
    # print (page.images)
    image_nums = len(page.images) # 含有图片数量

    count = 0 

    if image_nums == 0:
        print("文件中不包含图片文件")
    else:
        print(f'第{ page_num }页共{image_nums}张图片')
        print('-' *20)
        for img_file_obj in page.images:

            if image_nums > 1:  
                image_save_name_suffix = "_" + str(page_num) + "_" + str(count + 1)
                count += 1
            else:
                count = 1   
            
            # 图片保存路径
            image_save_path = os.path.join(save_dir, f'{os.path.basename(pdf_path).split(".")[0]}{ image_save_name_suffix }.png')

            with open(image_save_path, 'wb') as f:
                f.write(img_file_obj.data)
            time.sleep(0.2)
            print(f'--正在提取第{count}张图片--')
        print('-' * 20)
        print(f"第{ page_num }页提取完成")
        
    page_num += 1
    print("#" * 20)
    
time.sleep(2)
print("=" * 30)

# page = pdf_reader.pages[0]
# # print (page.images)
# image_nums = len(page.images) # 含有图片数量

# count = 0

# image_save_name_suffix = "" # 图片保存命名后缀编号

# if image_nums == 0:
#     print("文件中不包含图片文件")
# else:
#     print(f'总共{image_nums}张图片')
#     print('-' *20)
#     for img_file_obj in page.images:

#         if image_nums > 1:  
#             image_save_name_suffix = "_" + str(count + 1)
#             count += 1
#         else:
#             count = 1   
        
#         # 图片保存路径
#         image_save_path = os.path.join(save_dir, f'{os.path.basename(pdf_path).split(".")[0]}{ image_save_name_suffix }.png')

#         with open(image_save_path, 'wb') as f:
#             f.write(img_file_obj.data)
#         time.sleep(0.2)
#         print(f'--正在提取第{count}张图片--')
#     print('-' *20)
#     print("提取完成")
#     time.sleep(2)