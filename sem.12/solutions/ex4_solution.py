"""
Напишете рекурсивна функция, която приема низ като вход и връща булева стойност, показваща дали низът е палиндром или не.
"""


def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])


input_str = 'racecar'
output_bool = is_palindrome(input_str)
print(output_bool)
