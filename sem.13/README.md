Въведение в ООП
==============================================================================

## 0. Класове.

- Класът е план или шаблон за създаване на обекти. Той дефинира атрибутите и поведението, 
които обектите от този клас ще имат. Например, клас "Човек" може да има атрибути като "име", "възраст" и "пол" 
и поведение като "ходене" и "говорене". Класът определя как трябва да изглежда обект Person и какво трябва да може да прави. <br>
- В Python дефинираме клас чрез запазената дума ```class``` <br>
```python
class Person:
    pass
```


## 1. Обекти.

- Обектът е екземпляр на клас. Той е създаден въз основа на плана, предоставен от класа, и има свое собствено уникално състояние и поведение. 
Например, ако създадем два обекта от класа Person, "Ivan" и "Maria", всеки от тях ще има свои собствени уникални стойности за атрибутите "name", "age" 
и "gender". Всеки от тях би могъл също така да използва поведението „ходене“ и „говорене“, дефинирано от класа Person, по свои собствени уникални начини. <br>
```python
    personIvan = Person()
    personMaria = Person()
```


## 2. Атрибути.

- Атрибутите са променливи, които съхраняват данни в обект. Те представляват състоянието на обекта и могат да бъдат достъпни и модифицирани от 
методите на обекта. Например обект "Person" може да има атрибути като "name", "age" и "gender", които съхраняват информация за това лице. <br>
- Атрибутите на ниво обект се създават, когато даден обект се инстанцира от клас. Те са уникални за всяко копие на обекта и могат да бъдат 
достъпни и модифицирани с помощта на нотация с точки. Например, ако имаме клас "Person" с атрибут "name", можем да създадем атрибути на ниво обект, 
като инстанцираме нови обекти по следния начин:<br>
```python
class Person:
  def __init__(self, name):
    self.name = name

person1 = Person("John")
person2 = Person("Mary")) 
```

- Атрибутите на ниво клас са дефинирани в самия клас, но извън каквито и да е методи. Те се споделят от всички екземпляри на класа и могат 
да бъдат достъпни чрез нотация с точка в самия клас. Например, ако имаме клас "Person" с атрибут на ниво клас "species", можем да го дефинираме 
по следния начин:<br>
```python
class Person:
    species = "Homo sapiens"
    
    def __init__(self, name):
        self.name = name

print(Person.species)  # Output: "Homo sapiens"
Person.species = "Homo neanderthalensis" # променяме атрибута species
print(Person.species)  # Output: "Homo neanderthalensis"species
```


## 3. Методи.

- Методите са функции, които определят поведението на даден обект. Те могат да осъществяват достъп и да променят атрибутите на обекта, както и 
да извършват други операции. Например, обект "Person" може да има методи като "walk" и "talk", които определят как се държи лицето. <br>
- В Python има няколко вградени метода и атрибути, които обикновено се използват при дефиниране на класове и обекти: <br>

init метод: Методът "init" е специален метод в Python, който се използва за инициализиране на състоянието на обекта. 
Този метод се извиква, когато даден обект се инстанцира от клас, и ви позволява да зададете първоначалните стойности на атрибутите на обекта. 
Ето един пример: <br>
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("John", 30)
```
      
метод str: Методът "str" е друг специален метод в Python, който се използва за дефиниране на низовото представяне на обекта. 
      Този метод се извиква, когато обектът се отпечата или преобразува в низ с помощта на функцията str(). Ето един пример: <br>
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


person1 = Person("John", 30)
print(person1)  # Output: "John (30)"
```

## 4. Примерна задача за работа с клас.
```python
class BankAccount:
    def __init__(self, account_owner, account_number, balance=0):
        self.account_owner = account_owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")


account1 = BankAccount("Ivan", "123456", 1000)
account2 = BankAccount("Maria", "789012")

account1.deposit(500)  # Output: "Deposited 500. New balance is 1500."
account2.withdraw(1000)  # Output: "Insufficient funds."

```


## Задачи
1. Напишете клас на Python, който да представлява студент, с атрибути име, факултетен номер и списък с предмети (максимум 5), които посещава. След това създайте обекти от този клас за добавяне и премахване на предметите, които посещава.
2. Напишете клас за представяне на правоъгълник, който да съдържа методи за изчисляване на площта и периметъра на правоъгълник. Направете клас Point, който притежава за атрибути координатите x и y.
3. Напишете клас на Python за представяне на автомобил със следните изисквания:
- Класът трябва да има атрибути за марка, модел, година, цвят и текуща скорост.
- Класът трябва да има методи за стартиране на двигателя, ускоряване и спиране.
- Методът accelerate() трябва да приема параметър за количеството ускорение (в kmh) и съответно да актуализира текущия атрибут на скоростта.
- Методът brake() трябва да приема параметър за количеството спиране (в kmh) и съответно да актуализира текущия атрибут на скоростта. Ако силата на спиране е по-голяма от текущата скорост, скоростта трябва да бъде зададена на нула.
- Класът трябва да има метод str(), който връща низово представяне на обекта кола в следния формат: „Марка: {make}, Модел: {model}, Година: {year}, Цвят: {color}, Текуща скорост : {скорост} kmh".