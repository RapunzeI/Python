def prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True

print(prime(2))
print(prime(17))
print(prime(21))