# Напишете функция на Python, която приема низ като вход и
# връща неговото цяло число. Ако низът не може да бъде преобразуван
# в цяло число, функцията трябва да предизвика ValueError.

def str_to_int(input_str):
    try:
        return int(input_str)
    except ValueError:
        return "This string can't be converted to integer."

print(str_to_int('123'))
