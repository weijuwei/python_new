import requests

url = 'https://ss1.bdstatic.com/lvoZeXSm1A5BphGlnYG/skin/412.jpg'

res = requests.get(url)
res.raise_for_status() #检查是否成功，失败则停止

with open('test.jpg','wb') as f:
	for chunk in res.iter_content(10000):
		f.write(chunk)