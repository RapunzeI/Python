def rps(p1, p2):
    if p1==p2:
        return 0
    elif p1=='R':
        if p2=='P':
            return 1
        elif p2=='S':
            return -1
    elif p1=='P':
        if p2=='R':
            return -1
        elif p2=='S':
            return 1
    elif p1=='S':
        if p2=='R':
            return 1
        elif p2=='P':
            return -1

print(rps('R', 'P'))
print(rps('R', 'S'))
print(rps('S', 'S'))