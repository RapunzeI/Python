import math


def points(x, y, x1, y1):
    if x1-x != 0:
        slope = (y-y1)/(x-x1)
    else:
        slope = 'infinity'

    distance = math.sqrt((x1-x)**2+(y1-y)**2)

    print('The slope is {0} and the distance is {1}'.format(slope, distance))


points(0, 0, 1, 1)
points(0, 0, 0, 1)
