name = ''
while name != 'Tom':
    print("hello world!!!")
    name = input("please type your name :")
    if name == 'Tom':#当为True时会执行break 跳出本次循环，进入下次循环，死循环
        break
print("Thank you " + name) #此段永远不会执行
