# Напишете функция, която приема като параметър лист от цели числа и умножава всички елементи по 3. Използвайте map().

list_int_nums = range(-5,5)
result_mult_by_3 = list(map(lambda number: number * 3, list_int_nums))
print(result_mult_by_3)