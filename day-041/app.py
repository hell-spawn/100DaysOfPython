import random
from typing import Tuple

def die() -> int:
    return random.randint(1, 6)

# Simple version Craps
def craps() -> Tuple[int, int]:
    return ( die(), die() ) 


print(craps())

# Zonk game 

def zonk() -> Tuple[int, ...]:
    return tuple(die() for x in range(6))

print(zonk())

# Crarp to follow zonk desing
def craps_v2() -> Tuple[int, ...]:
    return tuple(die() for x in range(2))

print(craps_v2())

#Merge the two functions

def dice(n: int) -> Tuple[int, ...]:
    return tuple(die() for x in range(n))

print(dice(2)) # Craps
print(dice(5)) # Zonk 

def dice_v2(n : int = 2) -> Tuple[int, ...]:
    return tuple(die() for x in range(n))


print(dice_v2()) # Craps
print(dice_v2(5)) # Zonk 
