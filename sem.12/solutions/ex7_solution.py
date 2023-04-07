"""
Напишете функция, която приема два списъка с еднаква дължина като вход и използва zip, филтър и ламбда функция,
за да създаде нов списък само с елементите от първия списък, които са по-големи от съответния елемент от втория списък.
"""


def filter_elements(list1, list2):
    return list(filter(lambda x: x[0] > x[1], zip(list1, list2)))


list1 = [3, 7, 5, 9, 2]
list2 = [2, 8, 3, 8, 1]
output_list = filter_elements(list1, list2)
print(output_list)


