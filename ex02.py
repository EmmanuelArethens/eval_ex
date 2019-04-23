num = int(input('write a number'))
divby = int(input('check if its a multiple of'))
x = str(divby)

if num % divby == 0:
    print('your number is a multiple of' + x)
elif num % 4 == 0:
    print('your number is a multiple of 4')
elif num % 2 == 0:
    print('number is even')
else:
    print('number is odd')
