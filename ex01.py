listnames = []
listyear = []

def yearto100():

    name = input('Enter your name:')
    age = int(input('Enter your age'))
    x = str((2019 - age)+100)
    print('Hello, ' + name)
    print('you will turn 100 in the year ' + x)
    listnames.append(name)
    listyear.append(x)
    result = zip()
    resultlist = list(result)
    result = zip(listnames, listyear)
    resultSet = set(result)
    w = int(input("how many times do you want to show the result ?"))
    for i in range(w):
        print(resultSet)


yearto100()


