#solution_1
a = int(input())
b = int(input())

is_a_bigger = a > b
is_b_bigger = b > a

print(a * is_a_bigger + b * is_b_bigger)


#solution_2
a = int(input())
b = int(input())

is_first_bigger = a > b

print(a * is_first_bigger + b * (not is_first_bigger))


#solution_3- Kameliya
a = int(input())
b = int(input())

is_a_bigger = bool(a//b)
is_b_bigger = bool(b//a)

print(a * is_a_bigger + b * is_b_bigger)
