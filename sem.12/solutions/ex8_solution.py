"""
Напишете функция, която приема списък от редици като вход, където всяка редица съдържа цяло число и низ.
Функцията трябва да използва reduce, map и ламбда, за да създаде речник, където ключовете са уникалните низове в оригиналния списък,
а стойностите са сумата от целите числа в оригиналния списък, които съответстват на всеки низ.
"""


from functools import reduce


def sum_integers_by_string(input_list):
    unique_strings = set(x[1] for x in input_list)
    output_dict = {s: sum(x[0] for x in input_list if x[1] == s) for s in unique_strings}
    return output_dict


input_list = [(3, 'apple'), (5, 'banana'), (2, 'pear'), (7, 'banana'), (4, 'orange'), (8, 'apple'), (6, 'banana')]
output_dict = sum_integers_by_string(input_list)
print(output_dict)



