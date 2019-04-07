#!/usr/bin/python3

#类私有属性

class JustCounter:
    __secretCount = 0  ##__表示私有属性，只能供类内部使用
    publicCount = 0
    
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        
        print(self.__secretCount)

counter = JustCounter()
counter.count()

counter.count()

print(counter.publicCount)
print(counter.__secretCount) ##报错，取得私有属性