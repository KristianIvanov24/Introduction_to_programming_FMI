n = int(input())

basket = set()
for i in range(n):
    basket.add(input())

print(basket)

basket.remove('apple')
print(basket)

m = int(input())

fruits = set()
for i in range(m):
    fruits.add(input())

vegetables = basket - fruits
print(vegetables)

if "tomato" in vegetables:
    vegetables.remove("tomato")
else:
    vegetables.add("tomato")
    
if "cucumber" in vegetables:
    vegetables.remove("cucumber")
else:
    vegetables.add("cucumber")
    
if "zucchini" in vegetables:
    vegetables.remove("zucchini")
else:
    vegetables.add("zucchini")
    
print(vegetables)
