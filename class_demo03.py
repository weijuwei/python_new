#!/usr/bin/python3

class People: ##基类
    name = ''
    age = 0
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print("name: ",self.name,"\n",
               "age: ",self.age
            )
class Student(People): ##派生类
    stuid = ''
    
    def __init__(self,name,age,stuid):
        People.__init__(self,name,age)
        self.stuid = stuid
        
    def info(self):
        print("name: ",self.name,"\n",
               "age: ",self.age,"\n",
               "stuid: ",self.stuid
            )        

stu = Student('tom',23,"1232")
stu.info()            