import pyperclip,time
text = pyperclip.paste() #从剪贴板中读取内容赋值给text

lines = text.split('\n')
# print(lines)

for i in range(len(lines)):
	lines[i] = lines[i].replace("\r",'')
	if lines[i] == '':
		lines.remove(lines[i])  # 去除空元素

text = '-'.join(lines)  # 元素间添加-分隔符
print(text)

print("处理成功，右键粘贴到指定位置！！")
time.sleep(3)

pyperclip.copy(text) #写回剪贴板中