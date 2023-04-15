def superInteger(n, k):
    if len(n*k) == 1:
        return int(n)
    s = sum(int(digit) for digit in n) * k
    return superInteger(str(s), 1)

n = input()
k = int(input())

if int(n) < 1:
    print("Invalid values")
else:
    print(superInteger(n,k))
