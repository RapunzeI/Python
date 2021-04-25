def myGrep(filename, str):
    infile = open(filename)
    content = infile.readlines()
    infile.close()

    for line in content:
        if str in line:
            print(line, end='')

myGrep('example.txt', 'line')