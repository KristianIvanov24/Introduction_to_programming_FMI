class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_coordinates(self):
        return [self._x, self._y]

    def __str__(self):
        return f"Координати: ({self._x}, {self._y})"


class Rectangle(Point):
    def __init__(self, point=Point(), length=1, width=2):
        super().__init__(point._x, point._y)
        self._length = length
        self._width = width

    def center(self):
        center_x = self._x + self._length / 2
        center_y = self._y + self._width / 2
        return center_x, center_y

    def area(self):
        return self._length * self._width

    def circumference(self):
        return 2 * (self._length + self._width)

    def __str__(self):
        return f"Правоъгълник с точка A {super().__str__()}, дължина: {self._length}, ширина: {self._width}, център: {self.center()}, лице: {self.area()}, обиколка: {self.circumference()}"


rect = Rectangle(Point(1, 1), 10, 5)
print(rect)
