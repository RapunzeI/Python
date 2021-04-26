def arithmetic(lst):
    for i in range(len(lst)-2):
        if lst[i]+lst[i+2]!=2*lst[i+1]:
            return False
    return True

print(arithmetic([3, 6, 9, 12, 15]))
print(arithmetic([3,6,9,12,14]))
print(arithmetic([3]))