def roster(lst):
    print('{:10}{:10}{:10}{:10}'.format(
        'Last', 'First', 'Class', 'Average Grade'))
    for info in lst:
        print('{:10}{:10}{:10}{:8.2f}'.format(
            info[0], info[1], info[2], info[3]))


students = []
students.append(['DeMoines', 'Jim', 'Sophomore', 3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5])
students.append(['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympia', 'Edgar', 'Junior', 3.99])

roster(students)
