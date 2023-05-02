class Student:
    def __init__(self, name, age, current_class, grades):
        self.__name = name
        self.__age = age
        self.__current_class = current_class
        self.__grades = grades

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_current_class(self):
        return self.__current_class

    def set_current_class(self, current_class):
        self.__current_class = current_class

    def get_grades(self):
        return self.__grades

    def set_grades(self, grades):
        self.__grades = grades

    def calculate_average_grade(self):
        return sum(self.__grades) / len(self.__grades)


class School:
    def __init__(self, students):
        self.__students = students

    def get_students_with_grade_six(self, class_name):
        six_grade_students = filter(lambda student: student.get_current_class() == class_name and 5.5 <= student.calculate_average_grade(), self.__students)
        return list(six_grade_students)


student1 = Student("Alice", 15, "10A", [5, 6, 3, 4])
student2 = Student("Bob", 16, "10A", [6, 5, 5, 6])
student3 = Student("Charlie", 15, "10B", [6, 6, 6, 6])
student4 = Student("David", 16, "10B", [6, 5, 5, 6])
student5 = Student("Eve", 14, "10A", [6, 6, 6, 6])

school = School([student1, student2, student3, student4, student5])

students_10a_grade_six = school.get_students_with_grade_six("10A")

for student in students_10a_grade_six:
    print(student.get_name())
