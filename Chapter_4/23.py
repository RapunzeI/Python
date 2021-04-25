def average():
    text = input('Enter a sentence: ')
    text = text.split()
    sum=0
    
    for word in text:
        sum+=len(word)
    
    avg=sum/len(text)
    return avg

print(average())