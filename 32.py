integer = eval(input('Enter n: '))

first = integer//1000
integer = integer-first*1000

second = integer//100
integer = integer-second*100

third = integer//10

last = integer-third*10


print(first)
print(second)
print(third)
print(last)
