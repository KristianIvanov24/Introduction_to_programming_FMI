"""
Да се състави програма, която въвежда от клавиатурата целите числа p и q (p<q). Програмата да извежда простите числа в интервала [p,q].
Вход: 12 25
Изход: 13 17 19 23
"""


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def findPrimes(p, q):
    for i in range(p, q + 1):
        if (isPrime(i)):
            print(i)


findPrimes(12, 25)
