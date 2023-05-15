import numpy as np

arr = np.random.randint(1, 11, size=(3,3))

arr_sum = np.sum(arr)

row_means = np.mean(arr, axis=1)

col_std = np.std(arr, axis=0)

arr[arr % 2 == 0] = -1

arr_1d = arr.flatten()
arr_1d_sorted = np.sort(arr_1d)[::-1]
