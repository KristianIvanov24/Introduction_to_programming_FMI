class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1  
        self.p2 = p2 
        
    def width(self):
        return abs(self.p2.x - self.p1.x)
        
    def height(self):
        return abs(self.p2.y - self.p1.y)
        
    def area(self):
        return self.width() * self.height()
        
    def perimeter(self):
        return 2 * (self.width() + self.height())

    
p1 = Point(0, 0)
p2 = Point(3, 4)
rect = Rectangle(p1, p2)
print(rect.area()) 
print(rect.perimeter())  
