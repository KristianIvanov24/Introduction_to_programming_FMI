"""
Напишете функция, която приема като параметър лист и символен низ и връща като резултат индексът в листа, на който се намира низа. 
Ако низът не се среща в лист-а, върнете като резултат -1.
Вход: [a, b, c, d, myEl, e, 123], myEl
Изход: 4

Вход: [a, b, c, d, myEl, e, 123], asd
Изход: -1
"""


def findIndexInList(elements, toFind):
    if toFind in elements:
        return elements.index(toFind)
    else:
        return -1


print(findIndexInList(['a', 'b', 'c', 'd', 'myEl', 'e', 123], 'asd'))
