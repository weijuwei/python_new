import urllib.parse


dic = {'username':'tom','passwd':'1234567','page_num':12}
u = 'http://www.xxxxx.com/login?'

url = u + urllib.parse.urlencode(dic)

print(url)
#http://www.xxxxx.com/login?username=tom&passwd=1234567&page_num=12

#含有中文字符
dic1 = {"keyword":"曼联"}

u = 'http://www.xxxxx.com/query?'
url = u + urllib.parse.urlencode(dic1)
print(url)
#http://www.xxxxx.com/query?keyword=%E6%9B%BC%E8%81%94

var = '%E6%9B%BC%E8%81%94'
s = urllib.parse.unquote(var)#Replace %xx escapes by their single-character equivalent.
print(s) #曼联
