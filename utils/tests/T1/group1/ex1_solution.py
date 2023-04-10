import random as rnd 
list1 = [] 

for i in range(6): 
    list1.append(rnd.randint(2,10)) 


unique_elements_list = set(list1) 
unique_elements_list = list(unique_elements_list) 

result_dict = {} 

for item in unique_elements_list: 
    fact = 1 
    for i in range(2,item+1): 
        fact *= i 
    result_dict[item] = fact 

print(result_dict) 
