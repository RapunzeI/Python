def crypto(filename):
    infile = open(filename)
    content = infile.read()
    print(content.replace('secret', 'xxxxxx'))
    infile.close()

crypto('crypto.txt')