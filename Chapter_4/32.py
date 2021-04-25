def censor(fileName):
    infile = open(fileName)
    content = infile.read()
    infile.close()

    table = str.maketrans('.,:;!?', 6*' ')
    content = content.translate(table)
    content = content.split()

    for i in range(len(content)):
        if len(content[i])==4:
            content[i] = content[i].replace(content[i], 'xxxx')
    
    newfile = open('censored.txt', 'w')
    print(str(content), file=newfile)

censor('example.txt')