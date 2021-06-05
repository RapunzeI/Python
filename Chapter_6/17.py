def hexASCII():
    for i in range(ord('a'), ord('z') + 1):
        print(chr(i), ':', hex(i), end = ' ')

hexASCII()