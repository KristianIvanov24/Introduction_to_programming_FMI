N = {'hello': 100, 'b': 200, 'world': 300}
M = {'world': 300, 'b': 200, 'd': 400}
K = {}

# Не е добра практика да се изпозва i в такъв вид цикли, затова използваме думчики, които подсказват какво итерираме
for key in N.keys():
    K[key] = N[key] + M.get(key, 0)
                                          
for key in M.keys():
    if key not in K:
        K[key] = M[key]

print(K)
