# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re,time,random,string,os
from urllib.request import *
import urllib.error

total_page = 0 #图片的数量

picSrc_list = [] ##保存图片源地址的列表

url_list = []  #网页源内容列表

#创建一个10位长的随机字符串
def createRandomStr():
    words = string.ascii_letters + string.digits
    ran_str = ''
    for i in range(10):
        ran_str += random.choice(words)
    return ran_str

#传入一个url地址创建BeautifulSoup实例对象
def create_soup(url):
    headers = {
                'Host': 'www.mmonly.cc',
                'Referer': 'http://www.mmonly.cc/mmtp/qcmn/',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3738.0 Safari/537.36 Edg/75.0.107.0'
                }

    #读取网页源内容
    request = urllib.request.Request(url,None,headers)
    res = urllib.request.urlopen(request)
    html = res.read()    
    #创建一个BeautifulSoup对象实例
    soup = BeautifulSoup(html,'html.parser')
    return soup

#取得图片源地址保存到一个列表中
def get_picSrc(soup):
    ##取得图片所在源码标签段，根据不同网站可用不同的方法，此处查的是知乎的
    img_srcs = soup.select('.big-pic') 

    #print(img_srcs)
    for img in img_srcs:
        picSrc_list.append(img.find('img')['src'])
        print(img.find('img')['src'])
       

#下载图片保存到指定路径
def download_pic(picSrc_list):
    path = r'pic/' #存储路径 这里是相对路径
    #判断路径是否存在，不存在则创建
    if not os.path.exists(path):
        os.makedirs(path)

    print("共查找到%d张图片" %total_page)
    if total_page != 0:
        print("开始下载。。。")
        counter = 1 #计数

        for pic in picSrc_list:
            try:
               pic_name = '美女' + createRandomStr() #图片名字
               pic_path = path + pic_name + '.jpg'   #图片路径
               urlretrieve(pic,pic_path)
               print("正在下载第%d张图片" %counter)
            except Exception:
                print("下载第%d张图片失败！！！" %counter)

            time.sleep(2)    #休息2s
            counter += 1  
    else:
        print("没有图片可以下载。。。")
        return 0

url_id = '295258'   #http://www.mmonly.cc/mmtp/xgmn/295263.html 图片url中的一串数字
url_list.append('http://www.mmonly.cc/mmtp/xgmn/%s.html' %url_id)

try:
    #取得图片的数量
    total_page = int(create_soup(url_list[0]).select('.totalpage')[0].string)
    print("共有%d张" %total_page)

    #拼接url地址 并将指定url_id的所有页面加入到url_list列表中
    for index in range(2,total_page+1):
        url_list.append('http://www.mmonly.cc/mmtp/xgmn/%s_%s.html' %(url_id,str(index)))
        #print(url)
    
    print("请稍等,正在读取图片源地址。。。。。")

    # 读取图片的源地址
    for url in url_list:    
        get_picSrc(create_soup(url))
    print("读取完毕。")   
except Exception:
    print('读取失败！！！')

#print(picSrc_list)

download_pic(picSrc_list)