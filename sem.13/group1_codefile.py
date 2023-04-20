class Person:
    gender = 'not mentioned'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talking(self):
        return self.name + " говори много."

    def walking(self, km):
        return self.name + " изминава " + str(km) + " км на ден."

    def __repr__(self):
        return "Здравей, аз съм " + self.name + " и съм на " + str(self.age) + " години."


person1 = Person('Vili', 22)
person2 = Person('Pesho', 33)

print(person1.gender)
print(person1.__dict__)
# print(Person.__dict__)

print(person2.__dict__)
person2.gender = 'male'
print(person2.__dict__)
print(person2.gender)


