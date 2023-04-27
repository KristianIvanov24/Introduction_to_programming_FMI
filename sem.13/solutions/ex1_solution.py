class Student:
    def __init__(self, name, fn):
        self.name = name
        self.fn = fn
        self.classes = []
        self.max_classes = 5

    def add_class(self, course):
        if len(self.classes) < self.max_classes:
            self.classes.append(course)
        else:
            print("You have already reached the maximum number of classes.")

    def remove_class(self, course):
        if course in self.classes:
            self.classes.remove(course)
        else:
            print("You are not currently taking this class.")

    def __str__(self):
        return f"Name: {self.name}, FN: {self.fn}, Classes: {', '.join(self.classes)}"


my_student = Student("Ivan Ivanov", "0MI0000000")

# add classes
my_student.add_class("Abstract Algebra")
my_student.add_class("Calculus")
my_student.add_class("Introduction to programming")
print(my_student)

my_student.remove_class("English")

my_student.add_class("English")
my_student.add_class("Psychology")

my_student.add_class("Sports")

print(my_student)
