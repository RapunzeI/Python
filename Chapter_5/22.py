def pairSum(lst, n):
    for i in range(len(lst)):
        for k in range(i+1, len(lst)):
            if lst[i]+lst[k]==n:
                print(i, k)

pairSum([7,8,5,3,4,6], 11)