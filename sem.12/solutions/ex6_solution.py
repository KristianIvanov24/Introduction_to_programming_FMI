"""
Напишете функция, която приема списък от низове като вход и използва филтър и ламбда функция,
за да създаде нов списък само с низовете в оригиналния списък, които съдържат буквата "a".
"""


def filter_strings(input_list):
    filtered_list = list(filter(lambda s: 'a' in s, input_list))
    return filtered_list


input_list = ['apple', 'banana', 'pear', 'orange', 'grape']
output_list = filter_strings(input_list)
print(output_list)
