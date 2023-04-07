"""
Напишете функция, която приема речник като вход и връща списък от редици, където всяка редица съдържа ключа и стойността на речника.
"""


def dict_to_tuple_list(dictionary):
    return list(dictionary.items())


input_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
output_list = dict_to_tuple_list(input_dict)
print(output_list)
