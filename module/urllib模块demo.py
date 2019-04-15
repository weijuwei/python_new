import urllib.request
import urllib.parse
import urllib.error
import socket
import http.cookiejar
from urllib import error,request

# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# # print(data)
# res = urllib.request.urlopen('http://httpbin.org/post',data=data)  # POST请求 发送数据
# print(res.read())  # 输出响应响应信息
#
# res = urllib.request.urlopen('http://httpbin.org/get',timeout=1)  # GET请求
# print(res.read())
#
# print(res.status)  # 获取响应状态吗
# print(res.getheaders())  # 获取响应头
# print(res.getheader('Server'))
#
# try:
#     resp = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print("TIMEOUT")
#
# # Request
#
# head = {"User-Agent":"Firefox"}  #定义请求头部信息
# req = urllib.request.Request("http://httpbin.org/get",headers=head)
# res = urllib.request.urlopen(req)
# print(res.read().decode('utf-8'))

# cookie
filename = 'cookies.txt'

# #cookie保存
# cookie = http.cookiejar.CookieJar()
# cookie = http.cookiejar.MozillaCookieJar(filename)  # 将cookie信息保存到指定文件 cookie格式是MozillaCookie格式的
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# res = opener.open("http://www.baidu.com")  # 取得cookies
# cookie.save(ignore_discard=True,ignore_expires=True)
# for item in cookie:  # 遍历cookie信息
#    print(item.name+' = ' + item.value)

# # cookie读取
# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load(filename,ignore_expires=True,ignore_discard=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# res = opener.open("http://www.baidu.com")
# print(res.read().decode('utf-8'))

# 异常处理
try:
    res = urllib.request.urlopen("http://www.baidsu.com/sdsfadf.html")
    # print(res.status)
except error.HTTPError as e:
    print(e.reason,e.code,e.headers)
except error.URLError as e:
    print(e.reason)
else:
    print("Request Successed")