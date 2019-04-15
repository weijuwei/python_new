import requests
import random
import json

url_refer = 'http://toutiao.com'
url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=美女&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1554773765479'
# 定制请求头部 dict格式
headers = [{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'},
		   {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'},
		   {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}]

header = random.choice(headers)#随机选择一个请求头
resp = requests.get(url,headers=header)

data = resp.json()['data']
print(len(data),type(data))

print(type(data[0]))

for i in range(1,len(data)):
	if 'title' not in data[i]:
		continue
	print("---------------------我是分割线%d----------------------------" %i)
	print("title:",data[i]['title'])
	print("img_url:",data[i]['middle_image_url'])
	print("url：",url_refer+data[i]['seo_url'])
