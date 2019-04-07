from urllib import request
import re
import json

url = 'https://news.ifeng.com/c/7lb7MliIFlI'

html = request.urlopen(url)
content = html.read().decode()

#获取html源码中新闻内容的段落
article = re.findall(r'var allData = (.*}});',content)
new_str = article[0]

#string转json格式
new_json = json.loads(new_str)
#print(type(new_json))

new_title = new_json.get('docData').get('title') #取得新闻标题

new_content = new_json.get('docData').
					get('contentData').
					get("contentList")[0].
					get('data') #取得新闻内容
pattern = re.compile(r'<[/]?p>')
#print("新闻标题：",new_title)
new_con = re.sub(pattern,"\n",new_content) #替换<p>标签位换行"\n"

news = "新闻标题： " + new_title + "\n"+ new_con

print(news)
