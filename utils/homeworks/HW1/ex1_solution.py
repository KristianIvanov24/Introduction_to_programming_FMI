import math

a = float(input())
b = float(input())

if a <= 0 or b <= 0:
    print("Invalid data!")
else:
    s = a*b/2
    print(f"S = {int(s)}")

    c = math.sqrt(a**2 + b**2)
    print(f"c = {int(c)}")

    hc = b*a / c
    mc = 0.5 * c
    lc = math.sqrt(a*b - (a*b*c**2)/(a+b)**2)
    print(f"hc = {hc}, mc = {mc}, lc = {lc}")
