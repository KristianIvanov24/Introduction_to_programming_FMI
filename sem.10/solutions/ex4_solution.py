"""
Напишете рекурсивна функция, която намира n-тото число на Фибоначи (1, 1, 2, 3, 5, 8, ...)
Вход: 1
Изход: 1

Вход: 6
Изход: 8

Вход: -1
Изход: грешен вход!
"""


def fibonacci(n):
    if n < 0:
        return "грешен вход!"
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))
