def divisorsSum(num):
    sum = 0

    for i in range(1, num + 1):
        if num % i == 0:
            sum += i

    return sum


def sum_divisors_dict():
    result = {}

    for i in range(101, 1101):
        result[i] = divisorsSum(i)
    return result


def find_keys_with_same_value(divisor_sums):
    value_to_keys = {}
    for key, value in divisor_sums.items():
        if value not in value_to_keys:
            value_to_keys[value] = []
        value_to_keys[value].append(key)

    return value_to_keys


my_dict = sum_divisors_dict()
print(my_dict)
print(find_keys_with_same_value(my_dict))
