import json

# 四个方法
# json.dumps() 序列化一个obj为json格式字符串
# josn.dump() Serialize ``obj`` as a JSON formatted stream to ``fp``
# json.loads() 反序列化一个json格式字符串为一个python对象
# json.load() 从文件中读取并反序列化为一个json格式字符串

dic = {'name':'汤姆','age':'23','sex':'M'}
# print(dic,type(dic))

#序列化一个对象为json格式的字符串
json1 = json.dumps(dic,ensure_ascii=False,indent=4) 
print(json1,'\n',type(json1))

#将序列化后的json格式的stream写入文件中
# f = open('test.json','w',encoding='utf-8')
# json.dump(json1,f,ensure_ascii=False)
# f.close()

#反序列化
str1 = json.loads(json1)
print(str1,'\t',type(str1))

f = open('test.json','r',encoding='utf-8')
str2 = json.load(f)
print(str2,type(str2))
f.close()