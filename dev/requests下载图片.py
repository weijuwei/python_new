import requests,os,sys

url = 'https://ss1.bdstatic.com/lvoZeXSm1A5BphGlnYG/skin/412.jpg'

res = requests.get(url)
res.raise_for_status() #检查是否成功，失败则停止

total_size = int(res.headers['Content-Length']) # 取得图片大小
print(total_size)

temp_size = 0  # 已下载的大小

with open('test.jpg','wb') as f:
	for chunk in res.iter_content(chunk_size=1024):
		if chunk:
			temp_size += len(chunk)
			f.write(chunk)
			f.flush()

			# 下载进度条
			done = int(50 * temp_size / total_size)
			sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
			sys.stdout.flush()
print()