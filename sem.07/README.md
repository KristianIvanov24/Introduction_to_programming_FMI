# Съставни типове данни - продължение

## 1. Редици (tuples)

* Редиците се използват за съхраняване на голям брой данни в една променлива.
* Елементите в редиците са номерирани и за разлика от листите, елементите на редиците не могат да бъдат променяни след първоначалното им задаване.
* Tова означава, че също така не можем да добавяме и премахваме елементи към редиците.

```py
mytuple = ("apple", "banana", "cherry")
print(mytuple)

print(mytuple[1]) # "banana"
print(mytuple[1::]) # ("banana", "cherry")

mytuple[0] = "pineapple" # дава грешка

# Решение 1:
mytuple = list(mytuple)
mytuple[0] = "pineapple"
mytuple = tuple(mytuple)
print(mytuple)

# Решение 2 (само за добавяне на елементи):
tuple1 = ("apple", "banana", "cherry")
tuple2 = ("mango",) # запетая!!
tuple2 += tuple1
print(tuple2)

# Обхождане на редица:
for x in tuple2: 
    print(x) 
```

## 2. Множества (sets)

* Множествата се използват за съхраняване на голям брой данни в една променлива.
* Елементите на множествата са **неподредени, неиндексирани и не може да се променят**.
* Това значи, че може да се добавят нови елементи, могат и да се премахват елементи,
но един елемент не може да бъде променен, след като веднъж е добавен.
Това, че елементите са неиндексирани означава, че не може да има два елемента с еднаква стойност!
И последно, това че елементите са неподредени означава, че всеки път когато извикаме множеството, елементите могат да бъдат подредени по различен начин.

```py
myset = {"apple", "banana", "cherry"}
print(myset) # пуснете си програмата 2-3 пъти и вижте как поне веднъж ще са подредени различно

new_set = set() # празно множество

# Обхождане:
for items in myset:
    print(items)
```

### Основни методи:
- add()	Adds an element to the set
- clear()	Removes all the elements from the set
- copy()	Returns a copy of the set
- difference()	Returns a set containing the difference between two or more sets
- difference_update()	Removes the items in this set that are also included in another, specified set
- discard()	Remove the specified item
- intersection()	Returns a set, that is the intersection of two other sets
- intersection_update()	Removes the items in this set that are not present in other, specified set(s)
- isdisjoint()	Returns whether two sets have a intersection or not
- issubset()	Returns whether another set contains this set or not
- issuperset()	Returns whether this set contains another set or not
- pop()	Removes an element from the set
- remove()	Removes the specified element
- symmetric_difference()	Returns a set with the symmetric differences of two sets
- symmetric_difference_update()	inserts the symmetric differences from this set and another
- union()	Return a set containing the union of sets
- update()	Update the set with the union of this set and others

## Задачи

### Задача №1
Проведено е състезание по лека атлетика и треньорът на младежкия отбор записва резултатите (в секунди) от загрявката на всеки от участниците в състезанието. Ето и редицата:
```py
results = (("Megan", 22.4, 23, 22.8), ("Alan", 20.9, 20.3, 21), ("Tonny", 21, 21.1, 20.95))
```

Съставете програма, която: 
<br>
а) Пресмята средната стойност на всеки участник и извежда следния резултат в конзолата:
```py
(("Megan", 22.73), ("Alan", 20.73), ("Tonny", 21.02))
```
б) Подрежда във възходящ ред участниците в редицата спрямо техния среден резултат:
```py
(("Alan", 20.73), ("Tonny", 21.02), ("Megan", 22.73))
```
в) Извежда в подходящо съобщение резултатите от редицата:
```
Alan's average result from the competition is 20.73 s.
Tonny's average result from the competition is 21.02 s.
Megan's average result from the competition is 22.73 s.
```

### Задача №2

При подадена редица изведете в конзолата само уникалните стойности от нея.

### Задача №3

Създайте програма, която проверява дали точката А с координати (Xa, Ya) е вътрешна, външна или лежи на окръжност с радиус R и център на окръжността, съвпадащ с центъра на координатната система. (Xa, Ya и R се въвеждат от потребителя).

### Задача №4

Напишете програма, която:
- приема число N от потребителя
- потребителя въвежда N продукта, които се запазват в множество _**basket**_
- множеството се принтира на екрана
- от множеството се премахват всички променливи, които съдържат "apple" в себе си
- приема се число M от потребителя
- потребителя въвежда М вида плодове, които се запазват в множество _**fruits**_
- ако fruits e подмножество на basket, нека в _**vegetables**_ да се запише разликата на basket със fruits
- vegetables се принтира на екрана
- ако някой от следните низове се съдържа в vegetables да се премахне, а иначе да се добави:<br>
- - "tomato"
- - "cucumber"
- - "zucchini"
- vegetables се принтира отново
