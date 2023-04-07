"""
Напишете функция group_by_key, която приема списък от речници като вход и ги групира по определен ключ.
Функцията трябва да приема два аргумента: входния списък с речници и низ, представляващ ключа за групиране.
Функцията трябва да върне речник, където ключовете са уникалните стойности на посочения ключ във входните речници,
а стойностите са списъци с речници с тази ключова стойност.
"""


def group_by_key(lst, key):
    result = {}
    for d in lst:
        if key in d:
            if d[key] not in result:
                result[d[key]] = []
            result[d[key]].append(d)
    return result


input_list = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'New York'},
    {'name': 'David', 'age': 40, 'city': 'Boston'},
    {'name': 'Emily', 'age': 27, 'city': 'San Francisco'},
    {'name': 'Frank', 'age': 33, 'city': 'Boston'}
]

result = group_by_key(input_list, 'city')
print(result)
