"""
Да се състави програма, която въвежда от клавиатурата цяло число n в интервала (0,1000), пресмята двоичния му код, записва го в променлива и го извежда.
Вход: 123
Изход: 1111011
"""


def decimal_to_binary(decimal_num):
    binary_num = ""
    if decimal_num == 0:
        return "0"
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2
    return binary_num


print(decimal_to_binary(123))
