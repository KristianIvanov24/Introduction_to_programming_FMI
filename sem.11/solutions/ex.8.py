# Напишете функция, която вмъква стойност в сортиран масив
# (функцията очаква подадения масив да е сортиран), като след вмъкването, масивът остава сортиран.

def insert_element(array, n):
    array.append(n)
    array.sort()
    return array


array = [1, 20, 3]
array.sort()
print(insert_element(array, 3))


