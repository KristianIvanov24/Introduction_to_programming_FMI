my_tuple = 1, 2, 3, 3, 4, 4, 5, 5

unique_tuple = tuple(set(my_tuple)) #ако не кастнем към tuple() функцията set(my_tuple) ще ни върне dict, а функцията set() по подадени данни връща само уникалните ст-ти

print(unique_tuple)
