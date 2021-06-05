def letter2number(grade):
    score = {'A+':4.3, 'B+':3.3, 'C+':2.3, 'D+':1.3,
                'A':4, 'B':3, 'C':2, 'D':1, 'F':0, 'A-':3.7, 'B-':2.7, 'C-':1.7, 'D-':0.7}
    return score[grade]

print(letter2number('A-'))
print(letter2number('B+'))
print(letter2number('D'))