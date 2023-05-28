import pandas as pd
import numpy as np


# Създаване на класа Game с инфо за игрите
class Game:
    def __init__(self, console, name, review, score):
        self.console = console
        self.name = name
        self.review = review
        self.score = score

    def display_info(self):
        print(f"Game: {self.name}")
        print(f"Console: {self.console}")
        print(f"Review: {self.review}")
        print(f"Score: {self.score}\n")


# Зареждане на файла с информацията за игрите
df = pd.read_csv('games.csv')

# Създавне на празен лист за обектите от тип Game
games = []

# Обхождане на файла и записване като обекти от тип Game
for index, row in df.iterrows():
    game = Game(row['Console'], row['GameName'], row['Review'], row['Score'])
    games.append(game)

# Намиране на средната оценка на всички игри
scores = [game.score for game in games]
average_score = np.mean(scores)
print(f"Average Score: {average_score}\n")

# Намиране на играта с най-висока оценка
highest_score_game = max(games, key=lambda x: x.score)
print("Game with the Highest Score:")
highest_score_game.display_info()

# Намиране на броя игри за всяка конзола
console_counts = df['Console'].value_counts()
print("Number of Games Available for Each Console:")
print(console_counts)
print()

# Търсене на игра по име
search_name = input("Enter the name of the game you want to search for: ")
found_game = None

for game in games:
    if search_name.lower() in game.name.lower():
        found_game = game
        break

if found_game:
    print("Game Found:")
    found_game.display_info()
else:
    print("Game Not Found.")

# запазване и ъпдейтване на информацията за игрите във файла
df['Score'] = [game.score for game in games]
df.to_csv('games.csv', index=False)
