mult3 = {3 * i for i in range(100//3 + 1)}
mult5 = {5 * i for i in range(100//5 + 1)}
mult7 = {7 * i for i in range(100//7 + 1)}

print(mult5 & mult7)
print(mult3 & mult5 & mult7)
print(mult3|mult7)
print(mult3 ^ mult7)
print(mult7 - mult3)