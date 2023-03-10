# Задача №6 - опитайте сами
# Създайте програма, която конвертира едно цяло число от диапазона 0-255 от 10-ична в 16-ична бройна система.

# По време на упражнението определихме, че максималната стойност в този диапазон в 16-ична бройна система е FF,
# т.е. имаме максимум 2 позиции в резултата си

# ще използваме този стринг, като получения остатък при делението на 16 ще отговаря на индекс от стринга
str_16_elements = '0123456789ABCDEF'

result = ''
number = 243

# първи остатък

# временна променлива temp - съхранява целочисления резултат от делението (неправилно е да присвоим
# този резултат директно към number, защото ще искаме да използваме оригиналната
# стойност на number още веднъж в следващия ред)
temp = int(number / 16)

result += str_16_elements[number % 16] # oстатък 3

# след като вече нямаме повече действия с първ. стойност на number й присвояваме стойността на temp
number = temp

# втори остатък
temp = int(number / 16)
result += str_16_elements[number % 16] # остатък F
number = temp

# финалният резултат се образува от остатъците в обратен ред, затова обръщаме низа
print(result[::-1])