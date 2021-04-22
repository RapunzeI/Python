def pay(a, b):
    if b > 40:
        return 40*a+(b-40)*a*1.5
    else:
        return a*b


print(pay(10, 35))
print(pay(10, 45))
