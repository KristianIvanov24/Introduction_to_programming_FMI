import random as rnd
list1 = []

for i in range(6):
    list1.append(rnd.randint(2,10))


unique_elements_list = set(list1)
unique_elements_list = list(unique_elements_list)

result_dict = {}

for item in unique_elements_list: 
    sum = 1 # 1
    for i in range(2,item+1):
        sum += i
    result_dict[item] = fact

for item in unique_elements_list: 
    result_dict[item] = item*(item+1)/2

print(result_dict) # 1 1
