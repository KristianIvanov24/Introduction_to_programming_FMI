from diagonals_check import diagonals_check
from columns_check import columns_check
from rows_check import rows_check


def official_win(lst):

  if diagonals_check(lst) == False and columns_check(lst) == False and rows_check(lst) == False:
    return False
  else:
    return True
    
