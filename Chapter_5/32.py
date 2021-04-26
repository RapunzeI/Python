def fib(n):
    prevsum=0
    sum=1
    for i in range(n):
        sum+=prevsum
        prevsum=sum-prevsum

    return sum

print(fib(0))
print(fib(4))
print(fib(8))