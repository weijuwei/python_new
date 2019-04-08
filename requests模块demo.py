import urllib
import requests

##定制请求头部
headers = {
   			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
   		  }

url = 'http://www.mmonly.cc/mmtp/qcmn/295255.html'



html = requests.get(url,headers=headers)
html.encoding = 'gbk' #设置编码格式

status_code = html.status_code#检测响应状态码 如果是4xx 5xx的状态码会抛出异常
print(status_code)

data = html.text #取得响应的内容的文本形式
#print(data)

content = html.content##二进制响应内容
#print(content)

res_header = html.headers #查看一个以字典形式展示的服务器响应头
print(res_header)
print(res_header['Content-Type'])
