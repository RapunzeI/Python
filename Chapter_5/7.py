def xmult(aList, bList):
    lst=[]
    for i in aList:
        for k in bList:
            lst.append(i*k)

    return lst

print(xmult([2], [1,5]))
print(xmult([2,3],[1,5]))
print(xmult([3,4,1],[2,0]))