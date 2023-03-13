# Задача №2
# Напишете програма, при която:
#
# а) Потребителя въвежда число N, след това въвежда N цели числа, които се слагат в лист;
# б) Създава се нов лист, който съдържа само числата по-големи от 8;
# в) Създава се още един нов лист, който съдържа всички останали числа;
# г) Двата нови листа се принтират един след друг на нови редове.

n = int(input())

list1 = []

for i in range(n):
    number = int(input())
    list1.append(number)

list_greater_than_8 = []
other_items_list = []

for item in list1:
    if item > 8:
        list_greater_than_8.append(item)
    else:
        other_items_list.append(item)


print(list_greater_than_8)
print(other_items_list)