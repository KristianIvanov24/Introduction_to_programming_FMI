class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels
        
        
car = Car("Ford", "Mustang", 2022, 2)
motorcycle = Motorcycle("Harley Davidson", "Sportster", 2021, 2)

print(f"Car: {car.make} {car.model} ({car.year}) with {car.num_doors} doors")
print(f"Motorcycle: {motorcycle.make} {motorcycle.model} ({motorcycle.year}) with {motorcycle.num_wheels} wheels")
