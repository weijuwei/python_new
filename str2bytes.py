
str1 = "hello world,世界你好!!!"

# 将字符串转换位字节对象
b_str1 = str1.encode()
b_str2 = str.encode(str1)
print(b_str1)
print(b_str2)

# 指定编码格式
b_str3 = bytes(str1,encoding='utf-8')
print(b_str3)

# 将字节对象转换位字符串
str_b1 = bytes.decode(b_str1)
str_b2 = b_str2.decode()
print(str_b1)
print(str_b2)