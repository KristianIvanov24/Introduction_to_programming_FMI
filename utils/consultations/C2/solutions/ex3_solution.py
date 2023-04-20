def list_to_matrix(L, i=0):
    if len(L) - 2 == i:
        return [[L[i], L[i + 1]]]

    return [[L[i], L[i + 1]]] + list_to_matrix(L, i + 2)


print(list_to_matrix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
