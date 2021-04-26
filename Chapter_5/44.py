def encrypt(key, code):
    decode = ''
    for i in range(len(code)):
        decode+=key[int(code[i])]

    return decode

print(encrypt('3941068257', '132'))
print(encrypt('3941068257', '111'))