from bs4 import BeautifulSoup
from urllib import request
import re

url_s = 'http://www.pengfue.com/index_'
url_e = '.html'
pn = 0

f = open('xiaohua.txt','a+')

#print("开始抓取。。。")
while pn <= 10: 
	url = url_s + str(pn+1) + url_e
	html = request.urlopen(url).read().decode()
	#print(html)

	soup = BeautifulSoup(html,"html.parser")
#	print(soup.title.string + "第%d页 " %(pn+1))
	f.write("\n"+soup.title.string + "第%d页 " %(pn)+"\n")
#	print("-------------------------------------------------------------------------")
	content_list = soup.find_all(class_='content-img clearfix pt10 relative')
	#content_list = soup.find_all('dd')
	#print(content_list)

	for i,j in enumerate(content_list):
		print(i+1,"、",re.sub(r'\s+','',j.string))
		f.write(str((pn*10)+i+1)+"、"+re.sub(r'\s+','',j.string)+"\n")
	pn += 1
#	print("-------------------------------------------------------------------------")
#print("-------------------------------------------------------------------------")
f.close()
print("抓取完毕。。。")
	