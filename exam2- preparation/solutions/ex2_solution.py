def r(x, i=2):
    if x <= 1:
        return 0
    elif x % i == 0:
        return i + x // i + r(x // i, i)
    else:
        return r(x, i+1)

      
def DIC(n):
    d = {}
    for i in range(2, n+1, 2):
        d[i] = r(i)
    return d


print(DIC(10))
