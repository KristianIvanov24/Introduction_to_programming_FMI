# Типове грешки и тяхната обработка
## 1. Основни типове грешки 
### a) Syntax (синтактични)
* Python ще открие тези видове грешки, когато се опита да анализира вашата програма и ще излезе със съобщение за грешка, без да стартира нищо. 
* Синтактичните грешки са грешки при използването на езика Python и са аналогични на правописните или граматическите грешки в езика

Примери:
- оставяйки ключова дума;
- поставяне на ключова дума на грешното място;
- пропускане на символ, като двоеточие, запетая или скоби;
- правописна грешка на ключова дума;
- неправилен отстъп;
- празен блок.

```py
myfunction(x, y): 
    return x + y


else:
    print("Hello!")

if mark >= 50 
    print("You passed!")

if arriving:
    print("Hi!")
esle: 
    print("Bye!")

if flag:
print("Flag is set!") 
```

### б) Runtime (грешки по време на изпълнение)
* Програмата е без синтактични грешки -> изпълнява се от интерпретатора, но по време на изпълнение връща грешка

Примери за RuntimeError:
- деление на нула
- извършване на операция върху несъвместими типове
- използвайки идентификатор, който не е дефиниран
- достъп до елемент от списък, стойност в речника или атрибут на обект, който не съществува
- опит за достъп до файл, който не съществува

```py
alist = ["apple", "banana", "orange"]
for i in range(0, len(alist) + 1):  # IndexError: list index out of range
    print(alist[i])
```
### в) Logical (логически)
* програмата работи без срив, но дава неправилен резултат (грешката е причинена от грешка в логиката на програмата);

Примери:
- използване на грешно име на променлива
- отстъп на блок до грешно ниво
- използване на целочислено деление вместо деление с плаваща запетая
- грешно получаване на приоритет на оператора
- допускане на грешка в булев израз
- off-by-one и други цифрови грешки

```py
# Off-by-one error:
# for i in range (1, n) { ... } (n-1 times)
# for i in range (0, n + 1) { ... } (n+1 times)

# dividend = float(input("Please enter the dividend: "))
# divisor = float(input("Please enter the divisor: "))
# quotient = dividend / divisor
# quotient_rounded = math.round(quotient)

sum_squares = 0
for i in range(10):
    i_sq = i ** 2
sum_squares += i_sq

# Кое от тези две решения ще даде търсения от нас
# резултат на сбора от всички квадрати на числата от 1 до 10?

# Решение 1:
sum_squares = 0
i_sq = 0
for i in range(10):
    i_sq = i ** 2
sum_squares += i_sq 

# Решение 2:
sum_squares = 0
for i in range(10):
    i_sq = i ** 2
    sum_squares += i_sq 
```
## 2. Обработване на грешки
* Всички грешки по време на изпълнение (и синтаксис), на които сме се натъкнали, се наричат изключения (Exceptions)
* Всички изключения са подкласове на класа Exception
* Предимства при използването на този стил на обработка на грешки:
* * по-ефективен от блок от команди, при който се проверява за грешки (този блок от команди понякога може да е доста комплексен)
* * ясно очертава кой код ще се обработва за грешки и кой не

### a) try-except statement:

#### Пример 1:
```py
try:  # в този блок от команди се въвежда целия код, за който изпитваме съмнение, че ще ни върне грешка
    age = int(input("Please enter your age: "))
    print(f"I see that you are {age} years old.")
except ValueError:
    # при сриване на програмата заради грешка от тип ValueError програмата връща
    # "елегантно" съобщение, създадено от нас. При неправилен избор на типа грешка
    # в except блока програмата няма да го изпълни и ще се срине!!!
    print("Please enter a number!")
```

#### Пример 2:
```py
try:
    dividend = int(input("Please enter the dividend: "))
    divisor = int(input("Please enter the divisor: "))
    print(f"{dividend} / {divisor} = {dividend / divisor}")
except(ValueError, ZeroDivisionError):  # улавяне на повече от една грешка
    print("Oops, something went wrong!")
```

#### Пример 3:
```py
try:
    dividend = int(input("Please enter the dividend: "))
    divisor = int(input("Please enter the divisor: "))
    print(f"{dividend} / {divisor} = {dividend / divisor}")
except ValueError:
    print("The divisor and dividend have to be numbers!")
except ZeroDivisionError:
    print("The dividend may not be zero!")
```

#### Пример 4 (най-добрия от всички до момента):
```py
dividend = 0
divisor = 0
try:
    dividend = int(input("Please enter the dividend: "))
except ValueError:
    print("The dividend has to be a number!")

try:
    divisor = int(input("Please enter the divisor: "))
except ValueError:
    print("The divisor has to be a number!")

try:
    print(f"{dividend} / {divisor} = {dividend / divisor}")
except ZeroDivisionError:
    print("The dividend may not be zero!")
```
* По-добре е да използваме try-except при обработка на изключения в малки блокове от команди, за да сме прецизни при улавянето на грешки.

#### Интересен начин за улавяне на грешки, при който се изписва на кой ред е самата грешка:
```py
import sys

try:
    dividend = int(input("Please enter the dividend: "))
    divisor = int(input("Please enter the divisor: "))
    print(f"{dividend} / {divisor} = {dividend / divisor}")
except ValueError:
    print(f"The variable on line {sys.exc_info()[2].tb_lineno} has to be number!")
except ZeroDivisionError:
    print("The dividend may not be zero!")
```

### б) raise Exception
* raise се използва, ако искаме да хвърлим форматирано от нас изключение
```py
x = int(input())

if x < 0:
    raise Exception("Sorry, no numbers below zero")
else:
    print(x)
```

### в) try-else-finally
* добра практика, тъй като в блока try е обособен само и единствено реда, който може да предизвика грешка в програмата
* клаузата finally се изпълнява винаги без значение дали в кода е открита грешка или не, дали е обработена или не

```py
try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Hey, that wasn't a number!")
else:
    print(f"I see that you are {age} years old.")
finally:
    print("It was really nice talking to you. Goodbye!")
```
### Видове изключения и описание
<img width="736" alt="image" src="https://user-images.githubusercontent.com/114401128/209127777-c09dd1a9-71e6-450c-a410-87235d255124.png">

## Задачи
### Видове грешки
### Задача 1: 
Открийте грешките във всеки един блок от команди и коментирайте какъв тип грешка е допусната (Syntax, Runtime, Logical):

_Условие 1:_ Напишете програма, която при подадено цяло число n, принтира всяко число i между 1 и n.
```py
n = in(input("Моля, въведете число: "))
for i in range(1, n + 1)

prnt(i)
```
_Условие 2:_ Същото, но принтирайки само четните числа между 1 и n.
```py
for i in range(0, n + 1):
    if j % 2 == 0:
        print(j)
```
_Условие 3:_ Принтирайте числата между n и n^2, които се делят на 3.
```py
for i in range(n, n * n):
    if i % 3 == 1:
        print(i)
```

_Условие 4:_ Принтирайте сбора на числата между 1 и n^2.
```py
sum = 0
for i in range(1, n * n * n + 1):
    sum *= i

print(sum)
```

### Обработка на грешки
### Задача №1
Напишете програма на Python, която генерира произволно число между 1 и 10 и моли потребителя да познае числото. Ако потребителят въведе невалиден вход, обработете грешката с помощта на блок try-except.
### Задача №2
Напишете функция на Python, която приема две числа като вход и връща тяхното частно. Ако второто число е нула, функцията трябва да предизвика персонализирано изключение, наречено DivideByZeroError.
### Задача №3
Напишете функция на Python, която приема низ като вход и връща неговото цяло число. Ако низът не може да бъде преобразуван в цяло число, функцията трябва да предизвика ValueError.
### Задача №4
Напишете функция на Python, която приема списък с числа като вход и връща тяхната средна стойност. Ако списъкът е празен, функцията трябва да предизвика ZeroDivisionError.
