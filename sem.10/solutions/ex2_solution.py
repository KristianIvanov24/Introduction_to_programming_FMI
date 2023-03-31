"""
Напишете рекурсивна функция, която проверява дали едно естествено число е просто.
Проверете, дали наистина ви е подадено естествено число!
"""


def isPrime(n, i = 2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i+1 == n:
        return True

    return isPrime(n, i + 1)


print(isPrime(15))
