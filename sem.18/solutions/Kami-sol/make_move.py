def make_move(board, player):
  
    valid_move = False
    while not valid_move:
        row = int(input('Въведете номер на ред (0-2): '))
        col = int(input('Въведете номер на колона (0-2): '))
        print()
        position = row  * 3 + col

        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Невалидни координати. Опитайте отново. ( ͡ಠ ʖ̯ ͡ಠ)\n')
        elif board[position] != ' ':
            print('Това поле вече е заето. Опитайте отново. (งಠ_ಠ)ง\n')
        else:
            board[position] = player
            valid_move = True
