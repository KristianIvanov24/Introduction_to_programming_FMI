"""
По въведени от стандартния вход две цели числа да се изведе произведението в интервала между тях.
Вход: 5 10
Изход: 151200
"""


def intervalMulti(start, end):
    multi = 1
    for i in range(start, end + 1):
        multi *= i

    return multi


print(intervalMulti(5, 10))
