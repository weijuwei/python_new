import time

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return "名字：" + self.name.ljust(10) + "年龄：" + str(self.age)


class School:
    counter = 0  # 类属性，统计数量

    def __init__(self,name):  # 实例方法
        self.name = name
        self.students = []

    def __str__(self):
        return "学校名字是 " + self.name

    def add_stu(self,stu):
        if self.counter < 3:
            if stu.age < 5:
                print(stu.name + "年龄太小了,还没有到到达入学年龄")
            else:
                self.students.append(stu)
                self.set_counter()  # 调用一次 counter加一
        else:
            print("招生名额已满！！！"+ stu.name + "不能入学")

    def get_stu_info(self):
        for stu in self.students:
            print(stu.get_info())

    @classmethod
    def set_counter(self):  # 类方法
        self.counter += 1

sch = School('Tsinghua')
stu1 = Student("Tom", 3)
stu2 = Student("Jerry", 8)
stu3 = Student("Bob", 5)
stu4 = Student("Lucy", 7)
stu5 = Student("Lily", 7)
sch.add_stu(stu3)
sch.add_stu(stu1)
sch.add_stu(stu2)
sch.add_stu(stu4)
sch.add_stu(stu5)
print("---------------------")
print(sch.name+"学生数量是：",sch.counter)
print("---------------------")

sch.get_stu_info()
