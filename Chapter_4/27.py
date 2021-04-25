def fcopy(file1, file2):

    ffile = open(file1)
    sfile = open(file2, 'w', encoding = 'utf8')

    sfile.write(ffile.read())

    ffile.close()
    sfile.close()

fcopy('example.txt', 'output.txt')