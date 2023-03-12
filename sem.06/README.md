# Съставни типове данни

## 1. Списъци (list)

* Листите са колекция от елементи и се използват за съхраняване на голям брой данни в една променлива.

### Примери:
```py
mylist = ["apple", "banana", "cherry", "mango"]
mylist1 = ["apple", 15, True, "banana"]
mylist2 = [["apple", 15, True], False, "banana", -23.43]
```

* Достъп до елементи и слайсване - като при низовете
```py
mylist = ["apple", 15, True, "banana"]
print(mylist[-1]) # "banana"
print(mylist[1:3]) # [15, True]
```

* Основни методи <br>
```append()``` -  Adds an element at the end of the list <br>
```clear()``` -  Removes all the elements from the list <br>
```copy()``` - Returns a copy of the list <br>
```count()``` - Returns the number of elements with the specified value <br>
```extend()``` - Add the elements of a list (or any iterable), to the end of the current list <br>
```index()``` - Returns the index of the first element with the specified value<br>
```insert()``` - Adds an element at the specified position<br>
```pop()``` - Removes the element at the specified position<br>
```remove()``` - Removes the item with the specified value<br>
```reverse()``` - Reverses the order of the list<br>
```sort()``` - Sorts the list<br>

## 2. Речници (dict)

* Речниците се използват за съхраняване на голям брой данни в една променлива
* Елементите в речниците са подредени, могат да бъдат променяни след първоначалното им задаване, но не допускат повторения!
* Речниците имат ключове и стойности отговарящи на тези ключове.

```py
myDict = {'name': 'Emil', 'age': 30, 'student': False}
print(myDict)
print(myDict['name']) # достъп до стойност чрез ключа й
myDict['age'] = 31 # промяна на стойност на даден ключ
myDict['nationality'] = "Bulgarian" # добавяне на ключ и стойност
```

* Методи
```clear()``` - Removes all the elements from the dictionary <br>
```copy()``` - Returns a copy of the dictionary<br>
```fromkeys()``` - Returns a dictionary with the specified keys and value<br>
```get()``` - Returns the value of the specified key<br>
```items()``` - Returns a list containing a tuple for each key value pair<br>
```keys()``` - Returns a list containing the dictionary's keys<br>
```pop()``` - Removes the element with the specified key<br>
```popitem()``` - Removes the last inserted key-value pair<br>
```setdefault()``` - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value<br>
```update()``` - Updates the dictionary with the specified key-value pairs<br>
```values()``` - Returns a list of all the values in the dictionary<br>

## 3. Задачи

### Задача №1

Напишете програма, която: <br>
а) Намира най-голямото число в лист.<br>
б) Намира най-малкото число в лист.

### Задача №2
Напишете програма, при която:

а) Потребителя въвежда число N, след това въвежда N цели числа, които се слагат в лист; <br>
б) Създава се нов лист, който съдържа само числата по-големи от 8; <br>
в) Създава се още един нов лист, който съдържа всички останали числа; <br>
г) Двата нови листа се принтират един след друг на нови редове.<br>

### Задача №3
При подадени 5 цели числа от потребителя, намерете максимума и минимума, които могат да бъдат получени чрез сума на ТОЧНО 4 числа от 5те. След това принтирайте двете числа с " " между тях. <br>
(Hint: За целта използвайте list, и приложете функция над него :-) )

### Задача №4
Конвертирайте следния списък в речник:
```
[['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]
```
Желан резултат:
```
{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
```

### Задача №5
Напишете програма, която приема стойности от 1 до 10 като ключове в речник, чийто стойности са техните квадрати. (Визуализирайте получения речник в конзолата.)

### Задача №6
Напишете програма, която:

a) приема число N от потребителя <br>
б) приема N двойки (ключ-стойност) от потребителя, които се запазват в речник, като всеки път се проверява дали вече има такъв ключ в речника, и ако има такъв се принтира "key already exists" и се продължава нататък с въвеждането (без да се презаписва стойността!) <br>
в) речникът се принтира на екрана<br>

### Задача №7
Напишете програма, която приема вход два речника с дължини N и М от потребителя и създава нов речник, който обединява входните два, но събирайки стойностите, ако ключовете съвпадат.

Приемаме, че стойностите винаги са от тип integer, но това не важи за ключовете!

примерен вход: 
```py
3 3 
'hello’: 100, 'b': 200, ‘world': 300
'world': 300, 'b': 200, 'd': 400
```

примерен изход: 
```
{'world': 600, 'b': 400, 'd': 400, 'hello': 100}
```



