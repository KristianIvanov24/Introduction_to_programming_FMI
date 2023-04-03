# Напишете програма, която пресмята квадратите на първите N числа на фибоначи, използвайки map() функцията в решението.

def fib_func(counter, n1=0, n2=1, list_nums=[0, 1]):
    if counter == 0:
        return list_nums
    else:
        list_nums.append(n1 + n2)
        return fib_func(counter - 1, n2, n1 + n2, list_nums)


n = 5
fib_nums_list = fib_func(n)
print(list(map(lambda number: number ** 2, fib_nums_list)))
