s = '''It was the best of times, it was the worst of times; it
was the age of wisdom, it was the age of foolishness; it was the
epoch of belief, it was the epoch of incredulity; it was ...'''

table = str.maketrans('.,;\n', 4*' ')
newS = s.translate(table)

newS = newS.strip()

newS = newS.lower()

cnt = newS.count('it was')

newS = newS.replace('was', 'is')

listS = newS.split()

print(newS)
print(cnt)
print(listS)