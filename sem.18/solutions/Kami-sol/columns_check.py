from win_check import win_check

def columns_check(lst):
  for i in range (3): # 1, 2, 3
    lst1 = lst[i::3]
  
    if win_check(lst1):
      return True

  return False
