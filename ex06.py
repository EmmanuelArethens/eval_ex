x = input('type which word do u want to check as a palindrome')
w = ""

for i in x:
    w = i + w
    if (x==w):
        print("YES")

