# задача 1
import pandas as pd

# Зареждане на файла с данни
data = pd.read_csv('Popularity of Programming Languages from 2004 to 2023.csv')

# Въвеждане на имената на езиците, които искате да включите
chosen_languages = input("Въведете имената на езиците, които искате да включите (разделени със запетаи): ")
chosen_languages = chosen_languages.split(',')

# Извличане на данните за избраните езици
selected_data = data[['Date'] + chosen_languages]

# Извеждане на таблицата само с избраните езици
print(selected_data)


# задача 2
import pandas as pd
import matplotlib.pyplot as plt

# Зареждане на файла с данни
data = pd.read_csv('Popularity of Programming Languages from 2004 to 2023.csv')

# Въвеждане на имената на двата езика, които искате да сравните
language1 = input("Въведете името на първия език: ")
language2 = input("Въведете името на втория език: ")

# Извличане на данните за популярността на двата езика
language1_data = data[['Date', language1]]
language2_data = data[['Date', language2]]

# Начертаване на графика
plt.plot(language1_data['Date'], language1_data[language1], label=language1)
plt.plot(language2_data['Date'], language2_data[language2], label=language2)
plt.xlabel('Година')
plt.ylabel('Популярност')
plt.title('Сравнение на популярността на два езика')
plt.legend()
plt.show()



# задача 3
import pandas as pd

# Зареждане на файла с данни
data = pd.read_csv('Popularity of Programming Languages from 2004 to 2023.csv')

# Въвеждане на годината, която искате да анализирате
year = input("Въведете година: ")

# Извличане на данните за популярността за дадената година
year_data = data[data['Date'].str.contains(year)] #str.contains връша дали даден стринг се съдържа в друг

# Определяне на езика с най-голяма популярност
popularity_values = year_data.iloc[:, 1:]  # Маха 'Date' колоната
most_popular_language = popularity_values.idxmax(axis=1).values[0]

# Показване на най-популярния език за избраната година
print("Най-популярният език за година", year, "е:", most_popular_language)



# задача 4
import pandas as pd

# Зареждане на файла с данни
data = pd.read_csv('Popularity of Programming Languages from 2004 to 2023.csv')

# Изчисляване на средната популярност за всеки език
average_popularity = data.iloc[:, 1:].mean()

# Показване на резултатите
print(average_popularity)


# задача 5
from graphics import *
import pandas as pd

# Зареждане на файла с данни
data = pd.read_csv('Popularity of Programming Languages from 2004 to 2023.csv')

# Изчисляване на средната популярност за всеки език
average_popularity = data.iloc[:, 1:].mean()

# Сортиране на езиците по намаляващ ред на популярност
top_languages = average_popularity.sort_values(ascending=False)[:3]

# Създаване на прозорец
win = GraphWin("Топ 3 езика по популярност", 400, 400)

# Начални координати за първото кръгче
x = 150
y = 100

# Размер на кръгчетата
radius = 50

# Цветове за кръгчетата
colors = ['gold', 'silver', 'brown']

# Начертаване на кръгчетата с имената на езиците
for i, language in enumerate(top_languages.index):
    # Създаване на кръгче
    circle = Circle(Point(x, y), radius)
    circle.setFill(colors[i])
    circle.draw(win)

    # Добавяне на името на езика
    label = Text(Point(x, y), language)
    label.setSize(12)
    label.setTextColor('black')
    label.setStyle('bold')
    label.draw(win)

    # Промяна на координатите за следващото кръгче
    y += 2 * radius

# Очакване на клик за затваряне на прозореца
win.getMouse()
win.close()
