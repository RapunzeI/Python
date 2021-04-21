def negatives(lst):
    for i in lst:
        if i < 0:
            print(i)


print(negatives([4, 0, -1, -3, 6, -9]))
