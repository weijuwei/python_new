from urllib.request import *
import urllib.error
from bs4 import BeautifulSoup
import re

#headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
#}

url = 'https://new.qq.com/omn/20190406/20190406A05UNW.html'

request = urllib.request.Request(url)
res = urllib.request.urlopen(request)
html = res.read().decode('gbk')


##print(html)
soup = BeautifulSoup(html,'html.parser')


content = soup.select('.LEFT')

#取得内容的图片地址
img_label = content[0]('img')
img_src = img_label
print("文章中的图片链接是:")
for img in img_src:
	print("\thttp:%s" %(img['src']))

#取得新闻部内容
print(content[0].get_text())

#取得新闻内容
#content = soup.find_all('div',class_='content clearfix')
#print(content[0].get_text())
