"""
Напишете рекурсивна функция, която приема списък с цели числа като вход и връща нов списък с всички цели числа в оригиналния списък,
сортирани в низходящ ред.
"""


def descending_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        separator = input_list[0]
        left = [x for x in input_list[1:] if x >= separator]
        right = [x for x in input_list[1:] if x < separator]
        return descending_sort(left) + [separator] + descending_sort(right)


input_list = [4, 2, 8, 5, 1, 9, 3, 7, 6]
output_list = descending_sort(input_list)
print(output_list)
