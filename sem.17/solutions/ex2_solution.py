import math
from decimal import Decimal, getcontext

# задаване на точността на Decimal
getcontext().prec = 4

# изчисляване на площта на кръга с Decimal
radius = Decimal('2.5')
area_decimal = math.pi * radius ** 2

# закръгляне на резултата до 2 знака след десетичната запетая
area_decimal = area_decimal.quantize(Decimal('0.00'))

# изчисляване на площта на кръга с math
area_math = math.pi * radius ** 2

# закръгляне на резултата до 2 знака след десетичната запетая
area_math = round(area_math, 2)

# изчисляване на разликата
difference = area_decimal - area_math

# отпечатване на резултатите
print(f"Площта на кръга с Decimal: {area_decimal}")
print(f"Площта на кръга с math: {area_math}")
print(f"Разликата между площите: {difference}")
