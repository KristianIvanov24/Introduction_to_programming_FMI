"""
Да се изведат първите 20 естествени числа, двоичния запис на които съдържа равен брой 0 и 1
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

  
def equal_zeros_and_ones(n):
    binary = decimal_to_binary(n)
    count_ones, count_zeroes = 0, 0

    for number in binary:
        if number == '0':
            count_zeroes += 1
        else:
            count_ones += 1

    return count_ones == count_zeroes


for i in range(21):
    if equal_zeros_and_ones(i):
        print(i)
