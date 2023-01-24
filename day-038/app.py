"""
Using tuples
"""
from fractions import Fraction
from typing import NamedTuple

#Creating tuples use ()

my_data = ('Rice', Fraction(1/4), 'cups')

#Extracting items from a tuple
print(my_data[1])

# Using multiple assignment:
ingredient, amount, unit = my_data
print(ingredient) # >>>Rice
print(unit) # >>> cups

t = ('Kumquat', '2', 'cups')
#Here are some operations
print(len(t))
#How many times does a particular value appear in t?
print(t.count('2'))

#Which position has a particular value?
print(t.index('cups')) # >>>2
print(t[2]) # >>> 'cups'

#When an item doesn't exist, we'll get an exception:
#print(t.index('Rice')) # ValueError: tuple.index(x): x not in tuple

#Does a particular value exist?
print('Rice' in t) # >>> False

#Using NamedTuples

class Ingredient(NamedTuple):
    ingredient: str
    amount: str
    unit: str

item_2 = Ingredient('Kumquat', '2', 'cups')

print( f"Use {item_2.amount} {item_2.unit} fresh {item_2.ingredient}")
