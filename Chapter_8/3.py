class Rectangle:
    def setSize(self, width, length):
        self.width = width
        self.length = length
    def perimeter(self):
        return 2 * (self.width + self.length)
    def area(self):
        return self.width * self.length

rectangle = Rectangle()
rectangle.setSize(3, 4)
print(rectangle.perimeter())
print(rectangle.area())