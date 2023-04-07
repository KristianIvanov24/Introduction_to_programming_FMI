"""
Напишете функция, която приема списък от низове като вход и връща речник, където ключовете са низовете, а стойностите са дължината на низовете.
"""


def string_lengths(strings_list):
    return {s: len(s) for s in strings_list}


input_list = ['apple', 'banana', 'cherry']
output_dict = string_lengths(input_list)
print(output_dict)
