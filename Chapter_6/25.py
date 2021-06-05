def different(table):
    union = set()
    for i in table:
        union = union | set(i)
    return len(union)

t = [[1,0,1], [0,1,0]]
print(different(t))

t = [[32,12,52,63], [32,64,67,52], [64,64,17,34],[34,17,76,98]]
print(different(t))