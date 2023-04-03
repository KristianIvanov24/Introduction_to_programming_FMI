# Сравнете сумите на резултатите от задачи 4 и 5 и принтирайте по-голямата от тях на екрана.
import math
from functools import reduce
def fib_func(counter, n1=0, n2=1, list_nums=[0, 1]):
    if counter == 0:
        return list_nums
    else:
        list_nums.append(n1 + n2)
        return fib_func(counter - 1, n2, n1 + n2, list_nums)

def isPrime(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                return False

    return True

n = 10
fib_nums_list = fib_func(n)
fib_square_nums = list(map(lambda number: number ** 2, fib_nums_list))

even_square_fib_nums = list(filter(lambda fib_number: fib_number % 2 == 0, fib_square_nums))
prime_fib_nums = list(filter(isPrime, fib_nums_list))

sum_of_even_square_fib_nums = reduce(lambda x, y: x + y, even_square_fib_nums)
# print(sum_of_even_square_fib_nums) # 1224
sum_of_prime_fib_nums = reduce(lambda x, y: x + y, prime_fib_nums)
# print(sum_of_prime_fib_nums) # 112

print(sum_of_prime_fib_nums) if sum_of_prime_fib_nums > sum_of_even_square_fib_nums else print(sum_of_even_square_fib_nums)