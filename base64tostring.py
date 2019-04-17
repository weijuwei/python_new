import base64

str1 = 'weijuwei'

# base64编码
str1_b64 = base64.b64encode(str1.encode('utf-8'))

print(str1_b64) # b'd2VpanV3ZWk='
s = str(str1_b64,encoding='utf-8')  # 将bytes转换成string格式
print(s)

# base64解码
b64_str1 = base64.b64decode(str1_b64)
print(b64_str1)  # b'weijuwei'  # bytes格式

print(str(b64_str1,encoding='utf-8'))  # 转换为string格式