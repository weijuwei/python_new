from urllib.request import *
import re

url = 'https://news.ifeng.com/c/7laUtvhfWy7'
html = urlopen(url).read().decode()
content = re.findall(r'"contentData":{"contentList":\[{"data":"(.*)</p>","type":"text"}\]',html)
re = re.compile(r'<[^>]+>',re.S)
page = re.sub("\n",content[0])
print(page)