def no_spaces(board):
  for i in range(9):
    if board[i] == ' ':
      return False

  return True
