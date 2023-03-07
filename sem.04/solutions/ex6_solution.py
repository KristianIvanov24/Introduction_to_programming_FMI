type_of_degree = input("Въведи градусната мярка (C/F): ")
degree = float(input("Въведи градусите: "))

if type_of_degree == 'C':
    print(f"{degree} градуса по Целзий отговарят на {degree * 1.8 + 32} градуса по Фаренхайт.")
elif type_of_degree == 'F':
    print(f"{degree} градуса по Фаренхайт отговарят на {(degree - 32) / 1.8} градуса по Целзий.")
else:
    print("Invalid data!")
