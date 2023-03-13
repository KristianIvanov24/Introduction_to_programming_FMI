# Задача №1
# Напишете програма, която:
# а) Намира най-голямото число в лист.
# б) Намира най-малкото число в лист.
#

num_list = [-10, 3, -25, 10, 34, -100]
# вариант 1
num_list.sort()

print(num_list[-1])
print(num_list[0])

# вариант 2
print(max(num_list))
print(min(num_list))
