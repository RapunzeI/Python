def noVowel(str):
    for c in str:
        if c in 'aeiouAEIOU':
            return False
    return True


print(noVowel('crypet'))
