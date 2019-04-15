from urllib.request import *
import re

pic_url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E6%9B%BC%E8%81%94&pn=0&gsm=50&ct=&ic=0&lm=-1&width=0&height=0'

html = urlopen(pic_url)
obj = html.read().decode()

#print(obj)

urls = re.findall(r'"objURL":"(.*?)"',obj)

#print(urls)
i = 0
j = len(urls)
for url in urls:
	if i <= j:
		try:
			print("正在下载第%d张"%(i))
			urlretrieve(url,str(i)+'.jpg')
			i += 1
		except Exception:
			print("下载失败第%d张" %(i))
	else:
		print("图片下载完成!")
		break


##将获取的链接地址写入到文件中
#f = open('pic_url.txt','w+')
#for line in urls:
#	f.write(line+"\n")
#f.close()

