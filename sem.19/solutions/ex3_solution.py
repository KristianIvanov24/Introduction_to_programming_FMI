import numpy as np
import random as rd

size = rd.randint(1, 10)
matrix = np.random.randint(1, 300, (size, size)) #

print("Оригинална матрица:")
print(matrix)

filtered_matrix = np.where(matrix % np.power(matrix, 1/5) == 0, -1, matrix)

print("\nФилтрирана матрица:")
print(filtered_matrix)
