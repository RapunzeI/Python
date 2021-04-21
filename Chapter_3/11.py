def allEven(lst):
    for i in lst:
        if i % 2 != 0:
            return False
    return True


print(allEven([8, 0, -2, 4, -6, 10]))
print(allEven([8, 0, 1, 4, 6, 10]))
