def cheer(teamName):
    print('How do you spell winner?\nI know, I know!')
    for i in range(len(teamName)):
        print(teamName[i], end=' ')
    print('!\nAnd that\'s how you spell winner!\nGo {}!'.format(teamName))

cheer('Huskies')