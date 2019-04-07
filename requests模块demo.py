import urllib
import requests
from bs4 import BeautifulSoup

##定制请求头部
headers = {
   			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
   		  }

url = 'http://www.mmonly.cc/mmtp/qcmn/295255.html'

html = requests.get(url,headers=headers)
html.encoding = 'gbk' #设置编码格式

status_code = html.status_code#检测响应状态码 如果是4xx 5xx的状态码会抛出异常
print(status_code)

res_header = html.headers #查看一个以字典形式展示的服务器响应头
print(res_header)
print(res_header['Content-Type'])
'''
{'Date': 'Sun, 07 Apr 2019 09:34:46 GMT',
 'Content-Type': 'text/html', 
 'Transfer-Encoding': 'chunked', 
 'Connection': 'keep-alive', 
 'Vary': 'Accept-Encoding', 
 'P-State': 'ESOLC', 
 'Last-Modified': 'Sat, 06 Apr 2019 23:48:37 GMT', 
 'ETag': 'W/"5ca93ad5-4ee0"', 
 'Server': 'HiCDN', 
 'Expires': 'Mon, 08 Apr 2019 09:34:46 GMT', 
 'Cache-Control': 'max-age=86400', 
 'X-Cache-Status': 'HIT', 
 'XPage': '1d', 
 'Content-Encoding': 'gzip'}
'''


data = html.text #取得响应的内容
#print(data)

'''
soup = BeautifulSoup(data,'html.parser')
img_class = soup.select('.big-pic') 
img_label = img_class[0]
img_src = img_label.find('img')
print(img_src['src'])
'''

