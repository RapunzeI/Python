def mirror(word):
    dict = {'b':'d', 'd':'b', 'i':'i', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'q', 'q':'p', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x'}
    res = ''
    for ch in word:
        if ch not in dict:
            return 'INVALID'
        res += dict[ch]
    return res[::-1]

print(mirror('vow'))
print(mirror('wood'))
print(mirror('bed'))