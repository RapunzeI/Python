from random import *
def manhatten(x, y):
    street = [[0] * y for i in range(x)]

    row = x // 2
    col = y // 2
    street[row][col] = 1

    while True:
        dir = randint(0, 3) # 동서남북 : 0123

        if dir == 0: #동
            col += 1
        elif dir == 1: #서
            col -= 1
        elif dir == 2: #남
            row += 1
        else: #북
            row -= 1
        
        if row == x or row == -1 or col == y or col == -1:
            break

        street[row][col] += 1
    
    for i in street:
        print(i)

manhatten(5, 11)