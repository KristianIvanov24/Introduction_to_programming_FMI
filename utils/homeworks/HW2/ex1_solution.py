def LCM(a, b):
  temp = a % b
  if temp == 0:
        return a
  return a * LCM(b, temp) / temp

a = int(input())
b = int(input())

if a > 0 and b > 0:
    print(int(LCM(a, b)))
else:
    print("Invalid values")
