"""
Напишете рекурсивна функция, която пресмята НОД на две числа.
"""


def GCD(number1, number2):
    if number2 == 0:
        return number1
    return GCD(number2, number1 % number2)


print(GCD(16, 23124))
