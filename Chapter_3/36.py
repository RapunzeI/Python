def reverse_int(n):
    first = n//100
    second = (n-first*100)//10
    third = n % 10
    return third*100+second*10+first


print(reverse_int(123))
print(reverse_int(908))
