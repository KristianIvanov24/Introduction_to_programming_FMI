# Напишете функция на Python, която приема списък с числа като вход и
# връща тяхната средна стойност. Ако списъкът е празен, функцията
# трябва да предизвика ZeroDivisionError.

def mean_func(list_nums):
    result = 0
    for number in list_nums:
        result += number

    try:
        return result/len(list_nums)
    except ZeroDivisionError:
        return "The list is empty."
