import math

point_coordinates = xa, ya = int(input()), int(input()) #така директно въвеждаме двете точки в tuple, искаме ги в такъв формат, за да гарантираме, че няма да променим координатите на точката
r = int(input())

point = math.sqrt(point_coordinates[0]**2 + point_coordinates[1]**2)

if point > r:
    print("Външна")
elif point == r:
    print("Лежи на окръжността")
else:
    print("Вътрешна")
