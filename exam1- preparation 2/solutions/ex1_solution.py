n = int(input())

primes = []
for i in range(2, n+1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

for i in range(n):
    for number in primes:
        print(int(number**(i+1)), end=" ")
    print()
