def myBMI(weight, height):
    bmi=(weight*703)/height**2
    print(bmi)
    if bmi<18.5:
        print('Underweight')
    elif bmi<25:
        print('Normal')
    else:
        print('Overweight')
    
myBMI(190, 75)
myBMI(140, 75)
