import pickle

# dump(object, file)  将python对象转换成byetes格式并写入到文件中
# dumps(object) -> string 将python对象转换成bytes格式
# load(file) -> object 从文件中加载，转换成python对象
# loads(string) -> object 将bytes字符串格式转换成python对象

dic = {'name':'汤姆','age':'23','sex':'M'}

# pickle.dumps()
pic = pickle.dumps(dic)
print(pic,type(pic))

# pickle.loads()
pic2 = pickle.loads(pic)
print(pic2,type(pic2))

# f = open('test.pickle','wb')
# # pickle.dump(obj,fo)
# pickle.dump(dic,f)
# f.close()

f = open('test.pickle','rb')
pic3 = pickle.load(f)
f.close()
print(pic3,type(pic3))