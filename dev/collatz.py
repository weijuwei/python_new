def collatz(num):
    if num%2 == 0 :
        return num//2
    return 3*num +1
i = input("Please type a number:")
num = int(i)
print(num)

n = collatz(num)
while n != 1:
    print(n)
    n = collatz(n)
print(n)   