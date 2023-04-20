import random
import math

n = random.randint(5, 15)

numbers = []
for i in range(n):
    numbers.append(random.randint(0, 1000))

my_numbers = {}
for number in numbers:
    sqrt_num = int(math.sqrt(number))
    if sqrt_num**2 == number:
        my_numbers[number] = sqrt_num

print(my_numbers)
