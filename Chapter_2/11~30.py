# 11
import math
print(-(1+2+3+4+5+6+7))
print((9*17+10*24+11*21+12*27)/(17+24+21+27))
print(2**-20)
print(4356//61)
print(4365 % 61)

# 12
s1 = '-'
s2 = '+'

print(s1+s2)
print(s1+s2+s1)
print(s2+2*s1)
print(2*(s2+2*s1))
print(10*(s2+2*s1)+s2)
print(5*(s2+s1+3*s2+2*s1))

# 13
s = 'abcdefghijklmnopqrstuvwxyz'
print(s[0], s[2], s[-1], s[-2], s[s.index('q')])

# 14
s = 'goodbye'
print(s[0] == 'g')
print(s[6] == 'g')
print(s[0:2] == 'ga')
print(s[-1] == 'x')
print(s[7//2] == 'd')
print(s[0] == s[-1])
print(s[-1:-4] == 'tion')

# 15
print(len('anachronistically')+1 == len('misrepresentation'))
print('misinterpretation' < 'misrepresentation')
print('e' not in 'floccinaucinihilipilification')
print(len('counterrevolution') == len('counter'+'resolution'))

# 16
a = 6
b = 7
c = (a+b)/2
inventory = ['paper', 'staples', 'pencils']
first = 'John'
middle = 'Fitzgerald'
last = 'Kennedy'
fullname = first + ' ' + middle + ' ' + last

# 17
print(17+(-9) < 10)
print(len(inventory) > len(fullname)*5)
print(c <= 24)
print(a < 6.75 < b)
print(len(last) > len(middle) > len(first))
print(len(inventory) == 0 or len(inventory) > 10)

# 18
flowers = ['rose', 'bougainvillea', 'yucca',
           'marigold', 'daylilly', 'lilly of the valley']
print('potato' in flowers)
thorny = flowers[:3]
poisonous = flowers[-3:]
dangerous = thorny+poisonous

# 19
answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']
numYes = answers.count('Y')
numNo = answers.count('N')
percentYes = numYes/len(answers)
answers.sort()
f = answers.index('Y')

# 20
s = 'top'
print(s[::-1])

# 21
s = 'Minji'
t = 'Jeong'
print(s[0]+t[0])

# 22
lst = [3, 7, -2, 12]
print(max(lst)-min(lst))

# 23
monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsT = ('Jan', 'Feb', 'Mar', 'May')

monthsL.insert(3, 'Apr')
monthsL.append('Jun')
monthsL.pop()
monthsL.remove(monthsL[1])
monthsL.reverse()
monthsL.sort()

# 24
grades = ['B', 'B', 'F', 'C', 'B', 'A', 'A', 'D', 'C', 'D', 'A', 'A', 'B']
count = [grades.count('A'), grades.count('B'), grades.count(
    'C'), grades.count('D'), grades.count('F')]
print(count)

# 25
grades = ('B', 'B', 'F', 'C', 'B', 'A', 'A', 'D', 'C', 'D', 'A', 'A', 'B')
count = [grades.count('A'), grades.count('B'), grades.count(
    'C'), grades.count('D'), grades.count('F')]
print(count)

# 26
x = -7
y = 8
print(x**2+y**2 <= 100)

# 27
length = 20
angle = 0
angle = (math.pi * length)/180
height = length * math.sin(angle)
print(height)

# 28
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ab = lst[len(lst)//2]
lst.sort(reverse=True)
lst.remove(lst[0])
lst.append(lst[0])
lst.remove(lst[0])

# 29
print(0 == (1 == 2))
print(2+(3 == 4)+5 == 7)
print((1 < -1) == (3 > 4))

# 30
s = 'abcde'
s = list(s)
