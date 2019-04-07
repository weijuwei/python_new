import urllib
import requests

##请求头部
headers = {
   			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
   		  }

img_url = 'http://t1.hxzdhn.com/uploads/tu/201901/9999/b337cffadd.jpg'

#获取网页内容
img_res = requests.get(img_url,headers=headers)

img = img_res.content #响应的二进制格式内容
f = open('pic/02meinv.jpg','wb') #图片保存的路径
f.write(img) #写数据
print("图片下载成功")
f.close()  # 关闭文件