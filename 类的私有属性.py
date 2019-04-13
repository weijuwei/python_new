#!/usr/bin/python3

#类私有属性

class JustCounter:
    __secretCount = 0  ##__表示私有属性，只能供类内部使用
    publicCount = 0
    
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        
        print(self.__secretCount)

    def get_secretcounter(self): # 取得私有属性，可以供外部调用
    	return self.__secretCount

    def set_secretcounter(self,num): # 修改类私有属性，可以供外部使用
    	self.__secretCount = num    

counter = JustCounter()
counter.count()
counter.publicCount = 10 # 可以直接修改类公有属性

counter.set_secretcounter(5)  # 通过调用类函数修改私有属性
print(counter.publicCount)
print(counter.get_secretcounter()) ##通过调用类中定义的函数取得私有属性