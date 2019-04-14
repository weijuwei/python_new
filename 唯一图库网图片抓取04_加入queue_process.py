# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re, time, random, string, os
import requests
from multiprocessing import Process,Queue

total_page = 0  # 图片的数量
path = r'pic/'  # 存储路径 这里是相对路径
url_list = []  # 网页源内容列表


# 创建一个10位长的随机字符串
def createRandomStr():
    words = string.ascii_letters + string.digits
    ran_str = ''
    for i in range(10):
        ran_str += random.choice(words)
    return ran_str


# 传入一个url地址创建BeautifulSoup实例对象
def create_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }

    # 读取网页源内容
    html = requests.get(url, headers=headers)
    html.encoding = 'gbk'
    data = html.text
    # 创建一个BeautifulSoup对象实例
    soup = BeautifulSoup(data, 'html.parser')
    return soup


# 取得网页中目标图片的数量
def get_totalpage(soup):
    page_num = soup.select('.totalpage')
    totalpage = page_num[0].string
    num = int(totalpage)
    return num


# 向队列里面加入图片地址
def write(queue,url_list):
    for url in url_list:
        soup = create_soup(url)
        img_url = soup.select('.big-pic')[0].find('img')['src']
        print(img_url)
        queue.put(img_url)
        time.sleep(random.random())
    print("write:",queue.qsize())


# 从队列中取出地址下载图片
def read(queue):
    time.sleep(3)
    print(queue.qsize())
    while not queue.empty():
        pic = queue.get(True)
        pic_name = '美女' + createRandomStr()  # 图片名字
        pic_path = path + pic_name + '.jpg'  # 图片路径
        print("正在下载--------")
        print("队列数量：",queue.qsize())
        with open(pic_path,'wb') as f:
            f.write(requests.get(pic).content)
            f.close()
        time.sleep(1)


if __name__ == "__main__":

    # 判断路径是否存在，不存在则创建
    if not os.path.exists(path):
        os.makedirs(path)

    q = Queue() # 创建一个队列

    # http://www.mmonly.cc/mmtp/qcmn/290170_2.html
    # url_source = input("请输入网站url地址:")
    url_source = 'http://www.mmonly.cc/mmtp/qcmn/266848.html'

    url_split = url_source.split('/')  # 对输入的地址进行分割输出一个列表中
    pic_class = url_split[-2]  # 网站中美女图片所属分类 qcmn、xgmn、nymn、swmn、ctmn。。。
    url_id = (re.search(r'\d*', url_split[-1]).group())  # 使用正则再次分割取出.html的一串数字
    # print(url_id)

    url_list.append('http://www.mmonly.cc/mmtp/%s/%s.html' % (pic_class, url_id))

    total_page = get_totalpage(create_soup(url_list[0]))
    print("共有%d张" %total_page)

    for index in range(2,total_page+1):
        url_list.append('http://www.mmonly.cc/mmtp/%s/%s_%s.html' %(pic_class,url_id,str(index)))

    pw = Process(target=write,args=(q,url_list,))  #创建一个子进程向队列中写入数据
    pr = Process(target=read,args=(q,))  # 从队列中读取数据并下载
    pw.start()
    pr.start()
    pw.join()
    pr.join()