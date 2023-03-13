sum = 0

for i in range(15, 10000):
    if i % 3 == 0 and i % 5 == 0:
        sum += i

print(sum)
