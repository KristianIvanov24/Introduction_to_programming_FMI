"""
По въведено число n и намерете сумата на от n до 0;
Вход: 5
Изход: 1 + 2 + 3 + 4 + 5 = 15
"""


def sumFromN(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i

    print(sum)


sumFromN(5)
