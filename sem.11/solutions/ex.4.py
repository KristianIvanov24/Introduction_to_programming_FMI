# Филтрирайте резултата от задача 3, така че да останат само четните квадрати на първите N числа на фибоначи.

def fib_func(counter, n1=0, n2=1, list_nums=[0, 1]):
    if counter == 0:
        return list_nums
    else:
        list_nums.append(n1 + n2)
        return fib_func(counter - 1, n2, n1 + n2, list_nums)


n = 10
fib_nums_list = fib_func(n)
fib_square_nums = list(map(lambda number: number ** 2, fib_nums_list))

print(list(filter(lambda fib_number: fib_number % 2 == 0, fib_square_nums)))