#!/usr/bin/python3

#参数通过__init__()传递到类的实例化操作上
class Complex:
    def __init__(self,arg1,arg2):
        self.r = arg1
        self.i = arg2

x = Complex(3,5)
print(x.r,x.i)