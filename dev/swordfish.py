while True:
    print("Who are you ?")
    name = input()
    if name != 'Tom':#如果输入不是Tom，coninue语句将跳出循环回到开始处
        continue
    print('Hello,Tom. What is the password? (It is a fish)')
    password = input()
    if password == "swordfish":#如果满足条件,则跳出循环
        break
print("Access granted")
