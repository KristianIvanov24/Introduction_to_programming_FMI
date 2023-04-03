# Филтрирайте първите N числа на фибоначи, така че да останат само простите числа от тях
import math
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
print(list(filter(isPrime, fib_nums_list)))
