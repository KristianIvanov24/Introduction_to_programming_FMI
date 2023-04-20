n = int(input())
if n <= 0:
    print("Invalid data!")
else:
    for i in range(n, 1, -1):
        for k in range(n-i):
            print(" ", end="")
        for j in range(i):
            print(i**j, end=" ")
        print()

    for k in range(n-1):
        print(" ", end="")
    print("1")

    for i in range(2, n+1):
        for k in range(n-i):
            print(" ", end="")
        for j in range(i):
            print(i**j, end=" ")
        print()
