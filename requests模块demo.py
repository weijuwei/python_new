import requests
import random

url = 'http://www.qq.com'

# 定制请求头部 dict格式
headers = [{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'},
		   {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'},
		   {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}]

<<<<<<< HEAD
header = random.choice(headers)#随机选择一个请求头
print(header)
=======


html = requests.get(url,headers=headers)
html.encoding = 'gbk' #设置编码格式
>>>>>>> dev

#header = {'User-Agent':'weijuwei china dongguan'}
# html = requests.get(url,headers=header)

def get_src(url):
	def get_content():
		html = requests.get(url,headers=header)
		html.encoding = 'utf-8'
		return html
	return get_content	

get_html = get_src(url)

<<<<<<< HEAD
html = get_html()

content = html.text
print(content)

resp = html.headers
print(resp)
=======
res_header = html.headers #查看一个以字典形式展示的服务器响应头
print(res_header)
print(res_header['Content-Type'])
>>>>>>> dev
