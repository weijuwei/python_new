#!/usr/bin/python3
class MyClass:
    i = 12345
    #定义一个类函数
    def f(self):
        return 'hello world'

#实例化类
x = MyClass()

#访问类的属性和方法
print("Myclass类的属性i为：", x.i)
print("Myclass类的方法f输出为：",x.f())