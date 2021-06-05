def wordCount(text):
    text = text.split()
    counters = {}

    for word in text:
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1
    
    for item in counters:
        if counters[item] > 1:
            print(item + '\t' + 'appears', counters[item], 'times.')
        else:
            print(item + '\t' + 'appears', counters[item], 'time.')

text = 'all animals are equals but some animals are more equal than others'
wordCount(text)
