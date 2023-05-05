# Напишете програма на Python, която генерира произволно число между 1 и 10
# и моли потребителя да познае числото. Ако потребителят въведе невалиден вход,
# обработете грешката с помощта на блок try-except.

import random as rnd

random_number = rnd.randint(1,10)

user_number = 0  # neutral value

while random_number != user_number:
    try:
        user_number = int(input("Enter a number: "))
    except ValueError:
        print("Incorrect value!")
else:
    print("You find the number!")
