from urllib.request import *
from bs4 import BeautifulSoup
import re

# url = 'https://baike.baidu.com/item/%E6%9B%BC%E5%BD%BB%E6%96%AF%E7%89%B9%E8%81%94%E8%B6%B3%E7%90%83%E4%BF%B1%E4%B9%90%E9%83%A8/1631944?fromtitle=%E6%9B%BC%E8%81%94&fromid=73153'
url = 'https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD/1122445'
page = urlopen(url).read().decode()

'''
百科词条简介
<div class="lemma-summary" label-module="lemmaSummary">
 </div>
'''
html = BeautifulSoup(page,'html.parser')

# select()安装标签获取 返回list
str1 = html.select('.lemma-summary')
# print(str1[0])


str2 = str1[0]
# print(content)
dr = re.compile(r'<[^>]+>|\[[0-9]-?[0-9]?\]',re.S)
str3 = dr.sub('',str(str2))
print(str3)

'''
f = open('chelsea.txt','w+',encoding='utf-8')
f.write(str3)
f.close()
'''