def even(n):
    for i in range(2, n+1):
        if i % 3 == 0 or i % 2 == 0:
            print(i, end=', ')


even(17)
