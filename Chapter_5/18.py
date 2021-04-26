def four_letter(word):
    lst=[]
    for element in word:
        if len(element)==4:
            lst.append(element)

    return lst

print(four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust']))