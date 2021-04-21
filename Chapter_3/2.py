age = eval(input('나이를 입력하세요 : '))
if age >= 62:
    print("You can get your pension benefits")

name = input('이름을 입력하세요 : ')
nameList = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
if name in nameList:
    print('One of the top 5 baseball players, ever!')

hits = 11
shield = 0
if hits > 10 and shield == 0:
    print('You are dead...')

north = 0
south = 0
east = 0
west = 1

if north or south or east or west:
    print('I can escape.')
