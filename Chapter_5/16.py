def indexes(word, alpha):
    lst=[]
    for i in range(len(word)):
        if word[i]==alpha:
            lst.append(i)

    return lst

print(indexes('mississippi', 's'))
print(indexes('mississippi', 'i'))
print(indexes('mississippi', 'a'))