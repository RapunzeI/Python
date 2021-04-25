def stats(filename):
    infile = open(filename)
    content = infile.read()
    infile.close()

    lineCnt = len(content.split('\n'))

    wordList = content.split()
    wordCnt = len(wordList)

    charCnt = len(content)

    print(content.split('\n'))
    print('line count: {}'.format(lineCnt))
    print('word count: {}'.format(wordCnt))
    print('character count: {}'.format(charCnt))

stats('example.txt')