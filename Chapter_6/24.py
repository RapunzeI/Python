def names():
    nameDict = {}
    while True:
        name = input('Enter next name: ')
        if name == '':
            break
        elif name in nameDict:
            nameDict[name] += 1
        elif name not in nameDict:
            nameDict[name] = 1
    
    for i in nameDict:
        print('There is {} student named {}'.format(nameDict[i], i))

names()