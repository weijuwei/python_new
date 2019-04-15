from bs4 import BeautifulSoup
import re
from urllib import request
import time
from urllib.request import *
import random

url = 'https://www.zhihu.com/question/25509555'

path = r'picture/' #存储路径 这里是相对路径

html = request.urlopen(url).read().decode()
soup = BeautifulSoup(html,'html.parser')

print("标题： ",soup.title.string)

imag_src = soup.find_all('figure')
  #class__="origin_image zh-lightbox-thumb"))
imag_list = []
for i in imag_src:
    #print(i.find('img')['src'])
    imag_list.append(i.find('img')['src'])

print(imag_list)
print("共有%d张图片" %(len(imag_list)))
print("开始下载。。。")
img_counter = 0
for img in imag_list:
    time.sleep(1)
    try:
      #生成随机字符串作为图片存储名字
      pic_name = 'pic_' + ''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',12)) +'.jpg'

      pic_path = path + pic_name
      urlretrieve(img,pic_path)
      print("正在下载第%d张..." %(img_counter+1))
    except Exception:
      print("下载失败")
    img_counter += 1
print("下载完成。。。")