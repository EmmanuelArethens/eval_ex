num = int(input('write a number'))
number = str(num)
listmultiple = []

print("multiples of " + number + " are:")
for i in range(1, num +1):
    if num % i == 0:
        listmultiple.append(i)
        print(listmultiple)
