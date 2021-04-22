security = eval(input('Enter list of words: '))
for word in security:
    if word != 'secret':
        print(word)
