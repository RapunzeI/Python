class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

class Vector(Point):
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __repr__(self):
        return 'Vector{}'.format(self.get())

v1 = Vector(1, 3)
v2 = Vector(-2, 4)

print(v1 + v2)
print(v1 * v2)