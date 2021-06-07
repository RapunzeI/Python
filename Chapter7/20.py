def inValues():
    sum = 0
    cnt = 0
    while True:
        try:
            realNum = float(input('Please enter a number: '))
            if realNum == 0: return sum
            sum += realNum
        except:
            print('Error. Please re-enter the value.')
            cnt += 1
            if cnt == 2:
                return 'Two errors in a row. Quitting---'

print(inValues()) 