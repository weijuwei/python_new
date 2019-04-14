# 8位老师随机分配到三个办公室，保证每个办公室至少两个人

import random

teachers = ["赵大","钱二","孙三","李四","周五","吴六","郑七","王八"]
office_rooms = [[],[],[]]

for room in office_rooms:
    for i in range(len(office_rooms)-1):  # 循环，机选的人放到office中，并将机选的人从teachers中删除
        index = random.randint(0,len(teachers)-1)
        tea = teachers.pop(index)  # 将机选出的人从teachers中删除，并将结果赋值给tea
        room.append(tea)
        
for teacher in teachers:  # 将teachers中剩下的人随机放到office当中
    index = random.randint(0,2)
    office_rooms[index].append(teacher)

i = 1        
for room in office_rooms:  # 打印出分配结果
	print("办公室%d:" %i,end='\t')
	for teacher in room:
		print(teacher,end=" ")
	print()	
	i += 1