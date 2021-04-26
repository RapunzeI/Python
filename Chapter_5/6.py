def divisor(n):
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    return lst

print(divisor(1))
print(divisor(6))
print(divisor(11))
