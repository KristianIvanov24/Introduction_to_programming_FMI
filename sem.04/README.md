# Логически оператори. Условни конструкции. Задачи с условни конструкции

## 1. Логически оператори - припомняне

#### В едно от първите упражнения разгледахме операторите в Python и сега ще припомним тези, които ще използваме в днешното упражнение.

### a) Условни оператори

```py
x = 5
y = 12
print(x == y) # Equal
print(x != y) # Not equal
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
```

### б) Логически оператори
```py
x = 1
y = 2
z = 3
print(x < y and y < z)
print(x < y or y > z)
print(not(x > y or y < z))
```

### б) Оператори за идентичност и съдържание
```py
# оператори за идентичност
print(x is y)
print(x is not y)
print("")


# оператори за съдържане
s = "Obicham da ucha vuv fmi!"
print("fmi" in s)
s = "Obicham da ucha vuv fmi!"
print("fmi" not in s)
```

#### Тези оператори в комбинация с променливи могат да бъдат срещнати като условия в if - else конструкции

## 2. Условни конструкции 

#### Употреба: При разклонение на даден алгоритъм, като се изпълнява фрагмент код при верността или неверността на посоченото условие (т.е. if конструкцията ни връща булевите стойности _**True/False**_)

<img src="https://python-tricks.com/wp-content/uploads/2019/07/Conditional-Statements.jpg">

#### Пример: Взимане на чадър при дъжд (обсъждано по време на часа)

## 3. По-комплексни условни конструкции - практически задачи
### a) Разделяне на даден интервал на части
#### Искаме да направим скала за оценяване спрямо въведени точки в конзолата. Ще разпишем в Python следната скала:
* от 0 до 30 точки - 2
* от 31 до 50 - 3
* от 51 до 70 - 4
* от 71 до 85 - 5
* от 86 до 100 - 6

#### Трябва интервала от 0 до 100 да го разделим на части, посочени в скалата за оценяване. При въведена стойност (например 34) тя минава през всеки един от интервалите и влиза в този, при който се връща за първи път стойността True при проверката. При стойност 34 ще мине първо през интервала 0-30 и там ще върне False и така преминава през следващия интервал 31-50, където имаме True, изпълнява блока от команди и излиза от условната конструкция.
#### Наличието на повече от две разклонения се постига чрез ключовата дума ```elif```.

#### Ето го и решението на задачата:
```py
points = int(input("Enter points: "))
if 0 <= points <= 30:
    print(2)
elif 30 < points <= 50:
    print(3)
elif 50 < points <= 70:
    print(4)
elif 70 < points <= 85:
    print(5)
elif 85 < points <= 100:
    print(6)
else:
    print("Unvalid values")
```

### б) Вложени условни конструкции
```py
number = 5

if number >= 0:
    if number == 0:
      print('Number is 0')
    else:
        print('Number is positive')
else:
    print('Number is negative')
```

## 4. Задачи

### Задача №1

Напишете програма, която проверява дали един човек може да гласува. 
Като вход получавате възрастта на човека. 
<br> Hint: Всеки човек над 18 има право да гласува.

### Задача №2

Напишете програма, която проверява дали символ е гласна буква.
<br> Hint: гласните букви са: a, e, i, o, u, A, E, I, O, U

### Задача №3
При вход от потребителя цяло число, изпълнете следните условни действия:

а) Ако числото е нечетно - да се принтира “Odd”; 
<br> б) Ако числото е четно и е между 2 и 10 - да се принтира “Even between 2 and 10”; 
<br> в) Ако числото е четно и е между 11 и 20 - да се принтира “Even between 11 and 20”;
<br> г) Ако числото е четно и е по-голямо от 20 - да се принтира “Even over 20”.

### Задача №4

Създайте програма, при която след въвеждането на 3 числа върху конзолата се извежда:

а) най-голямото от тях <br>
б) най-малкото от тях <br>
в) средното по големина

### Задача №5 *

Напишете програма, която проверява дали една година е високосна или не.
<br> Hint: Една година е високосна, ако се дели на 4, или ако се дели на 100 трябва задължително да се дели и на 400.

### Задача №6

Напишете програма, която превръща градусите от Целзий във Фаренхайт и обратно, като изписва подходящо съобщение в конзолата. (Потърсете в интернет формулата за това превръщане).

примерен вход
```
Въведи градусната мярка (C/F): C
Въведи градусите: 32
```

примерен изход
```
32 градуса по Целзий отговарят на 89.6 градуса по Фаренхайт.
```
