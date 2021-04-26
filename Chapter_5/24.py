def pay(wage, hour):
    if hour<=40:
        return wage*hour
    elif hour<=60:
        return wage*40+wage*1.5*(hour-40)
    else:
        return wage*40+wage*1.5*20+wage*2*(hour-60)

print(pay(10,35))
print(pay(10,45))
print(pay(10,61))