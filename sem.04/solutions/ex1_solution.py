age = int(input())

if age >= 18:
    print("Can vote!")
elif 0 < age < 18:
    print("Can't vote")
else:
    print("Invalid data!")
