from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def operate(self, a, b):
        pass

class Adder(Calculator):
    def operate(self, a, b):
        return a + b

class Subtractor(Calculator):
    def operate(self, a, b):
        return a - b

class Multiplier(Calculator):
    def operate(self, a, b):
        return a * b

class Divider(Calculator):
    def operate(self, a, b):
        return a / b

      
a = 10
b = 5

adder = Adder()
print(adder.operate(a, b))  # Output: 15

subtractor = Subtractor()
print(subtractor.operate(a, b))  # Output: 5

multiplier = Multiplier()
print(multiplier.operate(a, b))  # Output: 50

divider = Divider()
print(divider.operate(a, b))  # Output: 2.0
