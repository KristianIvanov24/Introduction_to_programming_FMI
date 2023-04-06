"""
Напишете функция, която приема като параметър символен низ и връща като резултат същият низ, но наобратно.
Вход: hello, I am Dani
Изход: inaD ma I ,olleh
"""


def reverseString(to_be_reversed):
    return to_be_reversed[::-1]


print(reverseString('hello, I am Dani'))
