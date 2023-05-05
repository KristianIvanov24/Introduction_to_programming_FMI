# Напишете функция на Python, която приема две числа като вход и връща тяхното частнo.
# Ако второто число е нула, функцията трябва да предизвика персонализирано изключение,
# наречено DivideByZeroError.

def fraction_part(num1, num2):
    if num2 == 0:
        raise Exception("DivideByZeroError")
    return int(num1/num2)


print(fraction_part(3,0))
