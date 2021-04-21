team = ['Ava', 'Eleanor', 'Clare', 'Sarah']
tmp = team[0]
team[0] = team[-1]
team[-1] = tmp
print(team)
