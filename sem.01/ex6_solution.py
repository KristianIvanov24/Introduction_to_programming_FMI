"""
Задължително трябва да посочин типа при въвеждане. Също така посочваме типа и в отпечатването, 
защото ако беше само money/100 може да ни изпечата число с плаваща запетая. Вариант 2 е да го напишем
по следния начин money//100.
"""

money = int(input("Please input the the money you want to split: "))

print(f"{money//100}x100lv")
money %= 100

print(f"{money//50}x50lv")
money %= 50

print(f"{money//20}x20lv")
money %= 20

print(f"{money//5}x5lv")
money %= 5

print(f"{money//2}x2lv")
money %= 2

print(f"{money}x1lv")
