from official_win import official_win
from game_board import game_board
from make_move import make_move
from no_spaces import no_spaces
"""import numpy as np"""

"""def arr(lst):
  arr = np.asarray(lst)
  return arr"""

print("Привет, уважаеми играчи! ⸂⸂⸜(രᴗര๑)⸝⸃⸃\n\nПравилата са прости:\n1. Редувате се да поставяте своето символче.\n2. Първият направил комбинация с 3 последователни еднакви смволчета, печели!\n3. Комбинации:\n    1) 3 водаравно;\n    2) 3 хоризонтално;\n    3) 3 по диагонал.\n\nНека играта з а п о ч н е! ＼(￣O￣)\n")


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 'X'


while official_win(board) != True and no_spaces(board) != True:
  if player == 'X':
    player = 'O'
  else:
    player = 'X'

  game_board(board)
  print(f"\nХод на играч '{player}'")
  make_move(board, player)


game_board(board)

if official_win(board):
  print(f"\nИграч {player} п E ч Eл И! ＼(^o^)／")
else:
  print("\nРа ВеН с Т вО! ¯\_(ツ)_/¯\nОще е Д н А? (¬‿¬)")









  







