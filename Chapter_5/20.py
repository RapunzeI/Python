def intersect(fir, sec):
    lst=[]
    for i in fir:
        for k in sec:
            if i==k:
                lst.append(i)
                break
    return lst


print(intersect([3,5,1,7,9], [4,2,6,3,9]))