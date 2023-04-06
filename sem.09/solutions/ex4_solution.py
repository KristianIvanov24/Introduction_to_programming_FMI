"""
Напишете функция, която при подаден параметър N пресмята N! и го връща като резултат (N! -> N факториел)
Вход: 5
Изход: 120
"""


def fact(number):
    product = 1

    while number:
        product *= number
        number -= 1

    return product


print(fact(5))
