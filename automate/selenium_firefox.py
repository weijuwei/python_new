
from selenium import webdriver # 如果firefox没有安装在默认位置，就要手动指定位置 
location = 'D:/Program Files/Mozilla Firefox/firefox.exe' 
driver = webdriver.Firefox(firefox_binary=location) 
# 请求页面
driver.get("https://www.xiaoying.com/user/login") 
 # 通过css选择器获取相应元素 
jUsername = driver.find_element_by_css_selector('.jUsername') 
 # 填写前先清空 
jUsername.clear() 
 # 模拟系统按键 
jUsername.send_keys("18812345678") 
jPassword = driver.find_element_by_css_selector('.jPassword') 
jPassword.clear() 
jPassword.send_keys("pass123456") 
jSubmit = driver.find_element_by_css_selector('.jSubmit') 
 # 模拟点击登录按钮(这里帐号密码是乱填的，所以是登录不成功的） 
jSubmit.click() 
driver.close()
