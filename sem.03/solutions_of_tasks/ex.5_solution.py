# Задача №5
# Създайте програма, която конвертира едно цяло число от диапазона 0-255 от 10-ична в 8-ична бройна система.

# По време на упражнението определихме, че максималната стойност в този диапазон в осмична бройна система е 377,
# т.е. имаме максимум 3 позиции в резултата си
result = ''
number = 255

# първи остатък

# временна променлива temp - съхранява целочисления резултат от делението (неправилно е да присвоим
# този резултат директно към number, защото ще искаме да използваме оригиналната
# стойност на number още веднъж в следващия ред)
temp = int(number / 8)

result += str(number % 8) # остатък 7

# след като вече нямаме повече действия с първ. стойност на number й присвояваме стойността на temp
number = temp

# втори остатък
temp = int(number / 8)
result += str(number % 8) # остатък 7
number = temp

# трети остатък
temp = int(number / 8)
result += str(number % 8) # остатък 3
number = temp

# финалният резултат се образува от остатъците в обратен ред, затова обръщаме низа
print(result[::-1])