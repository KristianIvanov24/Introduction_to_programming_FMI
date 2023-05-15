from win_check import win_check

def diagonals_check(lst):
  
  for i in range (0, 3, 2): # 1, 2, 3
    lst1 = lst[i::4-i]
    
    if len(lst1) > 3:
      lst1.pop(3)
    
    if win_check(lst1):
      return True

  return False
