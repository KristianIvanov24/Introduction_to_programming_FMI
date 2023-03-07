a = int(input())
b = int(input())
c = int(input())

if a < b < c:
    print("Max number is:", c)
    print("Min number is:", a)
    print("Middle number is:", b)
elif a < c < b:
    print("Max number is:", b)
    print("Min number is:", a)
    print("Middle number is:", c)
elif b < c < a:
    print("Max number is:", a)
    print("Min number is:", b)
    print("Middle number is:", c)
elif b < a < c:
    print("Max number is:", c)
    print("Min number is:", b)
    print("Middle number is:", a)
elif c < a < b:
    print("Max number is:", b)
    print("Min number is:", c)
    print("Middle number is:", a)
elif c < b < a:
    print("Max number is:", a)
    print("Min number is:", c)
    print("Middle number is:", b)
else:
    print("They are even")
