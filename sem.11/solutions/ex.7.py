# Напишете функция, която проверява дали масив е сортиран в низходящ ред.

array = [23, 20, 7, 5, 1]
array_sorted = array.copy()
array_sorted.sort(reverse=True)
print(f"The array {array} is sorted in descending order.") if array == array_sorted else print(f"The array {array} is NOT sorted in descending order.")