"""
По въведено цяло число проверете дали то е просто. Изкарайте на стандартния изход подходящо съобщение.
"""


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


if isPrime(5):
    print("Prime Number!")
else:
    print("Non prime number!")
