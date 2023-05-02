from abc import ABC, abstractmethod

class Objects3D(ABC):
    def __init__(self):
        self._name = ""

    @abstractmethod
    def lsa(self):
        pass

    @abstractmethod
    def tsa(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Cube(Objects3D):
    def __init__(self, side):
        super().__init__()
        self._name = "Cube"
        self._side = side

    def lsa(self):
        return 6 * self._side * self._side

    def tsa(self):
        return 6 * self._side * self._side

    def volume(self):
        return self._side ** 3

class Pyramid(Objects3D):
    def __init__(self, base, height):
        super().__init__()
        self._name = "Pyramid"
        self._base = base
        self._height = height

    def lsa(self):
        return self._base * self._height / 2

    def tsa(self):
        return self._base * self._height / 2 + self._base ** 2

    def volume(self):
        return self._base ** 2 * self._height / 3

class Cylinder(Objects3D):
    def __init__(self, radius, height):
        super().__init__()
        self._name = "Cylinder"
        self._radius = radius
        self._height = height

    def lsa(self):
        return 2 * 3.14 * self._radius * self._height

    def tsa(self):
        return 2 * 3.14 * self._radius * (self._radius + self._height)

    def volume(self):
        return 3.14 * self._radius ** 2 * self._height
