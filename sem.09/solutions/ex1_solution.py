"""
Задача 1:
Напишете функция, която намира най-голямото от 3 числа.
Вход: 5 12 7
Изход: 12
"""


def largerstOfThree(num1, num2, num3):
    if num1 > num2 > num3 or num1 > num3 > num2:
        return num1
    elif num2 > num3 > num1 or num2 > num1 > num3:
        return num2
    elif num3 > num2 > num1 or num3 > num1 > num2:
        return num3
    else:
        return num1


print(largerstOfThree(5, 12, 7))
