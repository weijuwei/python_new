import random

money = 100
p_nums = 30

# i = 1

# list1 = []

# while i <= p_nums:
# 	s = random.uniform(0,money)
# 	list1.append(s)
# 	money = money - s
# 	if money == 0:
# 		break
# 	i += 1	

# print(list1,len(list1))	

sum_random = 0 #存放随机生成数的总和，计算权重使用
#random_list = []
random_dic = {}#存放每个人对应的红包

sum_ran = 0 #存放随机生成的（总红包数量减1数量）红包之和
last_person = 0 #存放最后一个红包

for i in range(1,p_nums):##生成比给定人数减1数量的随机数
	r = random.uniform(0,money)
	random_dic[i] = r
	sum_random += r

for j in random_dic:
	#( random_dic[j] / sum_random )计算权重
	mon = ( random_dic[j] / sum_random ) * money #权重乘以总钱数得到每个红包是多少
	random_dic[j] = mon

#print(random_dic)

sum1 = 0
for v in random_dic.values():
	sum_ran += int(v)
print(sum_ran)

last_person = money - sum_ran
print(last_person)

random_dic[p_nums] = last_person
print(random_dic)



