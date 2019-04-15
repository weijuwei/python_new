import requests
import random

url = 'http://www.qq.com'

# 定制请求头部 dict格式
headers = [{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'},
		   {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'},
		   {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}]

header = random.choice(headers)#随机选择一个请求头
# print(header)

html = requests.get(url,headers=header)
html.encoding = 'gbk' #设置编码格式

#header = {'User-Agent':'weijuwei china dongguan'}
#html = requests.get(url,headers=header)

def get_src(url):
	def get_content():
		html = requests.get(url,headers=header)
		html.encoding = 'utf-8'
		return html
	return get_content	

get_html = get_src(url)

html = get_html()

content = html.text
# print(content)

resp_header = html.headers #查看一个以字典形式展示的服务器响应头
# print(resp_header)
# print(resp_header['Content-Type'])

# 获取cookie信息
res = requests.get("https://www.baidu.com")
print("----------------------cookie")
for k,v in res.cookies.items():
	print(k+' '+v)
print("----------------------cookie")

# cookie设置
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/12324343")
res = s.get("http://httpbin.org/cookies")
print(res.text)


#发送cookies到服务器
url2 = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

re = requests.get(url2,cookies=cookies)
print(re.text)
print(re.url)

#传递URL参数字典格式 get请求
url3 = 'http://httpbin.org/get'
url_params = {'name':'tom','age':29}
r = requests.get(url3,headers=header,params=url_params)
print(r.url)  #结果是：'http://httpbin.org/get?name=tom&age=29'

url4 = 'http://httpbin.org/post'
#POST请求
##传入一个字典类型的数据
# rp = requests.post(url4,data=url_params)
# print(rp.text)
# '''
#   "form": {
#     "age": "29", 
#     "name": "tom"
#   },'''

#传入一个元组 相同的key对应不同的value
payload = (('key1', 'value1'), ('key1', 'value2'))
rp = requests.post(url4,data=payload,headers=header)
print(rp.text)
'''
  "form": {
    "key1": [
      "value1", 
      "value2"
    ]
  }'''


# 文件上传
files = {'file': open('test.json','rb')}
res = requests.post("http://httpbin.org/post",files=files,headers=header)
print(res.text)