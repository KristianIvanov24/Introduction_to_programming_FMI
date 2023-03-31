"""
Напишете рекурсивна функция, която приема списък, който съдържа само цели числа,
а) пресмята сумата на всички елементи в списъка
б) намира максималния елемент в списъка
в) намира минималния елемент в списъка
"""

#A
def listSum(lst, i = 0):
    if len(lst) == i:
        return 0
    return lst[i] + listSum(lst, i+1)


print(listSum([1,2,3,4]))


#Б
def findMaxElement(lst):
    if len(lst) == 1:
        return lst[0]

    max = findMaxElement(lst[1:])
    if lst[0] > max:
        return lst[0]

    return max


print(findMaxElement([1, 2, 3, 4]))



#B
def findMinElement(lst):
    if len(lst) == 1:
        return lst[0]

    min = findMinElement(lst[1:])
    if lst[0] < min:
        return lst[0]

    return min


print(findMinElement([1, 2, 3, 4]))
