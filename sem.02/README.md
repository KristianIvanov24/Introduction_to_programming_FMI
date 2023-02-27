# Низове - преговор, операции с низове

### от миналия път
```py
# едноредовите низове се отбелязват с единични или двойни кавички
print("Hello") 
print('Hello')

# при наличие на единична кавичка в низа е препоръчително той да има двойна затваряща и отваряща такава
print("Hello, I'm ...")

# конкатенация:
print("Hello" + "world!") # Helloworld!

# решения:
print("Hello" + " " + "world!")
print("Hello", "world!")
print(f"{"Hello"} {"world!"}")

# форматиране:
name = "Iva"
print(f"Hello, {name}!") # Hello, Iva!
```

### нови операции

## 1. Дължина на низ
```py
a_str = "Hello World!"
length = len(a_str)
print(length) # 12
```

## 2. Slicing
#### Всеки низ се разглежда като съвкупност от символи, разположени на определена позиция, наречена индекс. Чрез тази индексация достъпът до всеки символ от този тип примитивни данни е доста лесен и поражда разнообразие в съставянето на задачи.
![string indexing](https://res.cloudinary.com/practicaldev/image/fetch/s--A7oqOWqx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/1wr90mjnil60r7226bgq.png)
```py
a_str = "Hello world!"
print(a_str[0]) # 'H'
print(a_str[0] + a_str[-1]) # 'H!'

# string[start=0 : stop=len(string) : step=1]

print(a_str[0:5]) # 'Hello' <- в отрязания низ се включват символите от оригиналния низ на позиции от 0 до 4 вкл.
print(a_str[6::]) # 'world!'
print(a_str[6::2]) # 'wrd'
print(a_str[::-1]) # '!dlrow olleH'
print(a_str[4::-1]) # 'olleH' 
```
## 3. Основни методи
```py
s = "Hello world!"
print(s.upper()) # HELLO WORLD!
print(s.lower()) # hello world!

s = "      Hello world!            "
print(s) # принтира се с табулациите отпред и отзад
print(s.strip()) # принтира без разстояния отпред и отзад на текста

s = "hello world"
print(s.replace('l', 'e')) # 'heeeo wored'

s = "Hello world!"
print(s.split(" "))  # ['Hello', 'world!']
print(s.split("l"))  # ['He', '', 'o wor', 'd!']
```

## 4. Още един начин за форматиране на низ от символи
```
\" -> "
\' -> '
\\ -> \
!!!само в prompt в input функцията
\n -> нов ред
\t -> табулация
```
#### пример:
```py
print('Hello, I\'m Iva. I\'m from Burgas.')
```
