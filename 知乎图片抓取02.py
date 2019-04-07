from bs4 import BeautifulSoup
import re,time,random,string
from urllib import request
from urllib.request import *


words = string.ascii_letters + string.digits

path = r'picture/' #存储路径 这里是相对路径

#创建一个10位长的随机字符串
def createRandomStr():
    ran_str = ''
    for i in range(10):
        ran_str += random.choice(words)
    return ran_str

#读取网页源内容
def load_html(url):
    html = request.urlopen(url).read().decode()
    return html

#创建BeautifulSoup对象实例
def create_soup(html):
    soup = BeautifulSoup(html,'html.parser')
    return soup

#取得图片源地址保存到一个列表中
def get_picSrc(soup):
    picSrc_list = []  ##保存图片源地址的列表

    ##取得图片所在源码标签段，根据不同网站可用不同的方法，此处查的是知乎的
    img_srcs = soup.find_all('figure') 
    #print(img_srcs)
    for img in img_srcs:
        try:
            picSrc_list.append(img.find('img')['src'])
        except Exception:
            print("提取地址失败，请检查查找语句是否有问题！！")
            break
    return picSrc_list

#下载图片保存到指定路径
def download_pic(picSrc_list):
    total = len(picSrc_list) #图片数量
    print("共查找到%d张图片" %total)
    print("开始下载。。。")

    counter = 1 #计数

    for pic in picSrc_list:
        try:
           pic_name = 'pic_' + createRandomStr() #图片名字
           pic_path = path + pic_name + '.jpg'   #图片路径
           urlretrieve(pic,pic_path)
           print("正在下载第%d张图片" %counter)
        except Exception:
            print("下载第%d张图片失败！！！" %counter)

        time.sleep(1)    #休息1s
        counter += 1  

if __name__ == "__main__":
    html = load_html('http://www.zhihu.com/question/266808424/answer/626983318')
    soup = create_soup(html)
    imglist = get_picSrc(soup)
    download_pic(imglist)
