def factorial(n):
    f=1
    if n>0:
        for i in range(n,1,-1):
            f=f*i
    return f

print(factorial(0))
print (factorial(3))
print(factorial(5))