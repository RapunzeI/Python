def statement(fList):
    breakdown=[0,0]

    for money in fList:
        if money>0:
            breakdown[0]+=money
        elif money<0:
            breakdown[1]+=money
            
    return breakdown

print(statement([30.95, -15.67, 45.56, -55.00, 43.78]))
