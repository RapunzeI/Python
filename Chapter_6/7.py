def encoding(str):
    print('Char\tDecimal\tHex\tBinary')
    for ch in str:
        print(ch, '\t', ord(ch), '\t', hex(ord(ch)), '\t', bin(ord(ch)))

encoding('dad')