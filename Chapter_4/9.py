def words(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    table=str.maketrans('!,.:;?', '      ')
    content=content.translate(table)
    return content.split()

print(words('example.txt'))