def stringCount(filename, str):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    return content.count(str)

infile = open('example.txt', 'w', encoding='utf8')
print("line", file=infile)
print('line', file=infile)
print('line', file=infile)
print('line', file=infile)
infile.close()

print(stringCount('example.txt', 'line'))