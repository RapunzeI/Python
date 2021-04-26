def acronym(text):
    textList = text.split()
    shorten = ''
    for i in textList:
        shorten+=i[0]
    return shorten.upper()

print(acronym('Random access memory'))
print(acronym('central processing unit'))