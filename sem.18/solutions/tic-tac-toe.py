def print_board(board):
    print('   1   2   3')
    print('1  {} | {} | {} '.format(board[0][0], board[0][1], board[0][2]))
    print('  ---+---+---')
    print('2  {} | {} | {} '.format(board[1][0], board[1][1], board[1][2]))
    print('  ---+---+---')
    print('3  {} | {} | {} '.format(board[2][0], board[2][1], board[2][2]))
    print()


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def update_board(player, board):
    while True:
        try:
            print(f"It's player {player} turn!")
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1

            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                break
            else:
                print("Invalid input or cell already occupied. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

    board[row][col] = player


def play_game():
    print('Welcome to Tic-Tac-Toe!')
    print()

    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player = 'X'
    print_board(board)

    while True:
        update_board(current_player, board)
        print_board(board)

        if check_winner(board):
            print('Player', current_player, 'wins!')
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


play_game()
