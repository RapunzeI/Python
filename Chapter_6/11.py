def easyCrypto(str):
    res = ''
    for i in str:
        if ord(i) % 2 == 0:
            res += chr(ord(i) - 1)
        else:
            res += chr(ord(i) + 1)
    return res

print(easyCrypto('abc'))
print(easyCrypto('ZOO'))