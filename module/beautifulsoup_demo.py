html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,'html.parser')

## 输出html格式化样式
#print(soup.prettify())

#获取html <title>xxxx<title>
print(soup.title)
print(soup.title.string) #获取头部内容 不包含标签

print(soup.title.parent.name)

print(soup.find(id='link3')) #取得id为link3的标签

##输出所有<a></a> 返回类型为list
#print(soup.find_all('a'))

alist = soup.find_all('a')

#取得<a>包裹的内容和href链接
for a in alist:
	print(a.string," ",a.get('href'))

print(soup.get_text())	#获取文档中所有文本内容