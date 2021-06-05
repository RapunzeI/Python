def ticker(filename):
    dict = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if i % 2 == 0:
            key = lines[i].strip()
            value = lines[i + 1].strip()
            dict[key] = value
    for company in dict:
        print('Enter Company name : {0}\nTicker symbol:{1}'.format(company, dict[company]))

ticker('nasdaq.txt')