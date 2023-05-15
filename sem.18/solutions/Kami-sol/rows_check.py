from win_check import win_check

def rows_check(lst):

  for i in range (9): # 1, 2, 3
    if i % 3 == 0:
      lst1 = lst[i:i + 3]
  
    if win_check(lst1):
      return True

  return False
