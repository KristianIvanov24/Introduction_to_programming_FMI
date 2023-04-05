"""
Напишете функция, която приема число d и връща резултат колко от цифрите на d са му делители.
Вход: 124
Изход 3 (1 дели 124, 2 дели 124, 4 дели 124)

Вход: 111
Изход 3 (1 дели 111, 1 дели 111, 1 дели 111)

Вход: 10
Изход: 1 (1 дели 10, 0 не дели 10)
"""


def findDivisors(number):
    count = 0

    while number:
        divisor = number % 10
        if divisor != 0 and number % divisor == 0:
            count += 1
        number //= 10

    return count


print(findDivisors(10))
