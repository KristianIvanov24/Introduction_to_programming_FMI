"""
Напишете функция, която приема като параметър лист от символи и връща резултат символен низ, съдържащ символите от лист-а.
Вход: [H, e, l, l, o]
Изход: Hello 
"""


def listToString(lst):
    result_str = ''
    for element in lst:
        result_str += element

    return result_str


print(listToString(['H', 'e', 'l', 'l', 'o']))
