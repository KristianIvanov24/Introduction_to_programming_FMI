n = int(input())

num1 = 0
num2 = 1
print(num1, end=' ')
for i in range(n):
    print(num2, end=' ')
    num1, num2 = num2, num1 + num2
