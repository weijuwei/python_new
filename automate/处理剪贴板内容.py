##从剪贴板中读取几段文字，在每行开头添加*,
##然后在写会剪贴板中，手动粘贴

import pyperclip
text = pyperclip.paste() #从剪贴板中读取内容赋值给text

lines = text.split('\n')
for i in range(len(lines)):#循环读取每一行，添加*
	lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

print(text)
pyperclip.copy(text) #写回剪贴板中