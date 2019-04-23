import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a) & set(b)
print(c)

num = int(input('how much elements do you want in your two lists ? '))
l1 = random.sample(range(1, 10), num)
print(l1)
l2 = random.sample(range(1, 10), num)
print(l2)
result = set(l1) & set(l2)
resulstr = str(result)
print('you have' + resulstr + 'in common in your two lists')
