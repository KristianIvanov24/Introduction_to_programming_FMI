"""
Напишете функция, която приема като параметри лист, операция и число, като прилага операцията върху всеки елемент от листа с втори аргумент подаденото число.
Вход: [1, 2, 3, 7, 5, 4, 0] + 2
Изход: [3, 4, 5, 9, 7, 6, 2]
Вход: [5, 5, 1, 6] * 12
Изход: [60, 60, 12, 72]
(Hint: не се изисква потребителя да ни подава лист, можем да си зададем лист, който да използваме за да тестваме)
"""


def changeListBy(numbers, aritmetic_operation, number):
    result_numbers = []
    for num in numbers:
        if aritmetic_operation == '+':
            result_numbers.append(num+number)
        elif aritmetic_operation == '-':
            result_numbers.append(num-number)
        elif aritmetic_operation == '*':
            result_numbers.append(num*number)
        elif aritmetic_operation == '/':
            result_numbers.append(num/number)
    return result_numbers


print(changeListBy([5, 5, 1, 6], '*', 12))
