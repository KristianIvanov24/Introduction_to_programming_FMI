class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age


class Worker(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary


class Company:
    def __init__(self):
        self.__workers = []

    def add_worker(self, worker):
        self.__workers.append(worker)

    def print_workers(self):
        for worker in self.__workers:
            print(worker.get_name(), worker.get_age(), worker.get_salary())

    def is_worker_in_company(self, name):
        for worker in self.__workers:
            if worker.get_name() == name:
                return True
        return False

    def print_worker_info(self, name):
        for worker in self.__workers:
            if worker.get_name() == name:
                print("Name: ", worker.get_name())
                print("Age: ", worker.get_age())
                print("Salary: ", worker.get_salary())


worker1 = Worker("Alice", 25, 5000)
worker2 = Worker("Bob", 30, 7000)
worker3 = Worker("Charlie", 20, 4000)

company = Company()
company.add_worker(worker1)
company.add_worker(worker2)
company.add_worker(worker3)

company.print_workers()

print(company.is_worker_in_company("Bob"))
print(company.is_worker_in_company("David"))

company.print_worker_info("Alice")
