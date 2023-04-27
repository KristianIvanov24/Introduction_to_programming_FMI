class Person:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address
        
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        self.__age = age
        
    def get_age(self):
        return self.__age
    
    def set_address(self, address):
        self.__address = address
        
    def get_address(self):
        return self.__address
    
    def get_info(self):
        return f"{self.__name}, {self.__age}, {self.__address}"
    
    
person1 = Person("John Doe", 25, "123 Main St.")
person1.set_age(26)

person2 = Person("Jane Smith", 30, "456 Oak St.")
person2.set_address("789 Pine St.")

print(person1.get_info())
print(person2.get_info())
