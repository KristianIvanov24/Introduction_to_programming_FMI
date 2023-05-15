def win_check(lst):
  wins = True
  for i in range (1, len(lst)):
    if lst[i - 1] != lst[i] or lst[i] == ' ':
       wins = False
    
  if wins:
    return True

  return False
