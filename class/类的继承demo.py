#!/usr/bin/python3

class People: ##基类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print("name: ",self.name,"\n",
               "age: ",self.age
            )
class Student(People): ##派生类    
    def __init__(self,name,age,stuid):
        super().__init__(name,age)
        # People.__init__(self,name,age)
        self.stuid = stuid
        
    def info(self):
        print("name: "+self.name+"\n"
               "age: "+str(self.age)+"\n"
               "stuid: "+self.stuid
            )        

stu = Student('tom',23,"1232")
stu.info()            