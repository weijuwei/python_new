#!/usr/bin/python3

class Student:
    name = ''
    age = 0
    sex = ''
    
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def info(self):
        print("name:",self.name,"\n"
              "age: ",self.age,"\n"
              "sex: ",self.sex
             )
#实例化Student类
stu = Student('Tom',23,'M')
stu.info()
 