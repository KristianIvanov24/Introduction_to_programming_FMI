'''
## Задача №1
Напишете програма, която:
* генерира случайно цяло число в интервала [5,15] и го присвоява на променливата number
* добавя към празен речник следната двойка ключ-стойност:
{number: [сумата на числата от 1 до number, произведението на числата от 1 до number]}
'''

import random

number = random.randint(5, 15)

dict1 = {}

sum = 0
mult = 1
for i in range(1, number + 1):
    sum += i
    mult *= i

dict1.update({number: [sum, mult]})
print(dict1)
