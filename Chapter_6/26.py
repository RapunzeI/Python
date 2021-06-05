def week():
    weekDick = {'Mo':'Monday', 'Tu':'Tueday', 'We':'Wednesday', 'Th':'Thursday', 'Fr':'Friday', 'Sa':'Saturday', 'Su':'Sunday'}

    while True:
        day = input('Enter day abbreviation: ')
        if day == '': break
        print(weekDick[day])

week()