def duplicate(filename):
    infile = open(filename)
    content = infile.read()
    infile.close()

    table = str.maketrans('.,!:;?', 6*' ')
    content = content.translate(table)
    content = content.split()

    for i in range(len(content)):
        for j in range(i+1, len(content)):
            if content[i]==content[j]:
                return False

    return True

print(duplicate('example.txt'))
print(duplicate('output.txt'))