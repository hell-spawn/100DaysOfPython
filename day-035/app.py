"""Numbers Python"""

import decimal
import math
import sys

# Big number python 
print(math.factorial(52))

#For some of the details on the internals of integers

print(math.log(sys.maxsize, 2)) # 63-bit values for small integers.
print(sys.int_info) # 30-bit digits, and each of these digits occupies 4 bytes.

"""
Types Numbers
- Float
- Decimal
- Fraction
"""

"""Decimals"""
from decimal import Decimal


tax_rate = Decimal('7.25')/Decimal(100)
purchase_amount = Decimal('2.95')
total_amount = tax_rate * purchase_amount # It's computed with decimal places

print(total_amount)
penny = Decimal('0.01')

total_amount = purchase_amount + tax_rate * purchase_amount 
print(total_amount)
print(total_amount.quantize(penny)) #To round to the nearest penny and  default rounding rule of ROUND_HALF_EVEN.
print(total_amount.quantize(penny, decimal.ROUND_UP))

"""Fraction calculations"""
from fractions import Fraction
sugar_cups = Fraction('2.5')
scale_factor = Fraction(5/8)
print(sugar_cups * scale_factor) # >>> Fraction(25, 16)

"""Floating-point approximations"""
answer = (19/155)*(155/19)# >>> 0.9999999999999999
print(answer)
print(round(answer, 3)) # >>> 1.0

#math.isclose() function to compare two floating-point values
print((19/155)*(155/19) == 1.0) # >>> Flase
print(math.isclose((19/155)*(155/19), 1)) # >>> True



"""True division and floor division"""

#Doing floor division

total_seconds = 7385
hours = total_seconds // 3600 #  // Floor division
remaining_seconds = total_seconds % 3600 
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")

# Alternative 

total_seconds = 7385
hours, remaining_seconds = divmod(total_seconds, 3600)
minutes, seconds = divmod(remaining_seconds, 60)
print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")

# Doing true division
total_seconds = 7385
hours = total_seconds / 3600
print(round(hours, 4)) # >>> 2.0514

# Rational fraction calculations

from fractions import Fraction

total_seconds = Fraction(7385)
hours = total_seconds / 3600 # Fraction(1477, 720)
print(hours) # 2.0514
round(float(hours),4) 


