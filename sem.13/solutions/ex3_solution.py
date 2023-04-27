class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def start_engine(self):
        print(f"{self.make} {self.model} engine started.")

    def accelerate(self, kmh):
        self.speed += kmh
        print(f"{self.make} {self.model} accelerated to {self.speed} kmh.")

    def brake(self, kmh):
        if kmh >= self.speed:
            self.speed = 0
        else:
            self.speed -= kmh
        print(f"{self.make} {self.model} slowed down to {self.speed} kmh.")

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Current Speed: {self.speed} mph."


my_car = Car("Ford", "Mustang", 2022, "Red")

my_car.start_engine()    

my_car.accelerate(30) 
my_car.accelerate(20)    

my_car.brake(40)
my_car.brake(15)        

print(my_car)  
