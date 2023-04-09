def F(N, x):
    if N == 0:
        return 1
    elif N == 1:
        return x
    else:
        return (x**2)*F(N-1, x) - F(N-2, x)


print(F(4, 0.5))
