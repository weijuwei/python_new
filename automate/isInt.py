num = input('please input a number:')
try:
    int(num)
    print(num)
except ValueError:
    print('You type was ' + num)
    print('You must type a int!!')
