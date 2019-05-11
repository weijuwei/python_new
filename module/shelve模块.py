# shelve可以将python程序中的变量保存到二进制的shelf文件中，
# 程序可以从磁盘中恢复变量的数据

import shelve

sf = shelve.open('mydata')
# names = ['Tom','Jerry','Lucy']
# age = [23,24,34]
# sf['names'] = names  # 将列表保存到sf数据文件中
# sf['age'] = age
# print(sf['names'])  # 取得已经保存的变量数据
# print(sf['age'])

print(list(sf.keys()))  # 取得保存的keys
print(list(sf.values()))  # 取得保存的数据

sf.close()