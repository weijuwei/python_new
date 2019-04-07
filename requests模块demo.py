import urllib
import requests
from bs4 import BeautifulSoup

##定制请求头部
headers = {
   			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
   		  }

url = 'http://www.mmonly.cc/mmtp/qcmn/295255.html'

html = requests.get(url,headers=headers)
html.encoding = 'gbk'

data = html.text
#print(data)
soup = BeautifulSoup(data,'html.parser')
img_class = soup.select('.big-pic') 
img_label = img_class[0]
img_src = img_label.find('img')
print(img_src['src'])

