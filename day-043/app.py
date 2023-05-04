from re import U
from typing import Tuple, List, Union, Set
import random


# Writing list-related type hints

scheme = [
        ('Brick_Red', (198, 45, 66)),
        ('color1', (198.00, 100.50, 45.00)),
        ('color2', (198.00, 45.00, 142.50)),
        ]

# Function without typing
def hexify(r: float, g: float, b: float) -> str:
    return f'#{int(r)<<16 | int(g)<<8 | int(b):06X}'

def source_to_hex(src):
    return [ (n, hexify(*color)) for n, color in src ]
ColorCode = Tuple[str, str]
ColorList = List[ColorCode]

RGB_I = Tuple[int, int, int]
RGB_F = Tuple[float, float, float]

ColorRGB = Tuple[str, Union[RGB_I, RGB_F]]
ColorRGBList = List[ColorRGB]

def source_to_hex_typing(src: ColorRGBList) -> ColorList:
    return [
      (n, hexify(*color)) for n, color in src
    ]

print(source_to_hex_typing(scheme))

"""
create set objects.
Literal: 
    b = {value, value, ...} 
    b = set()

Conversion Function: 
    b = set(myList)

Add Method:
    b = set()
    b.add(value)

Comprehension: 
    b = {value for item in list_items }

Generator Expression: 
    b = set(value for imte in list_items)
"""

import collections
from typing import Collection


import_details = [
('Chapter_12.ch12_r01', ['typing', 'pathlib']),
('Chapter_12.ch12_r02', ['typing', 'pathlib']),
('Chapter_12.ch12_r03', ['typing', 'pathlib']),
('Chapter_12.ch12_r04', ['typing', 'pathlib']),
('Chapter_12.ch12_r05', ['typing', 'pathlib']),
('Chapter_12.ch12_r06', ['typing', 'textwrap', 'pathlib']),
('Chapter_12.ch12_r07', ['typing', 'Chapter_12.ch12_r06', 'Chapter_12.ch12_r05', 'concurrent']),
('Chapter_12.ch12_r08', ['typing', 'argparse', 'pathlib']),
('Chapter_12.ch12_r09', ['typing', 'pathlib']),
('Chapter_12.ch12_r10', ['typing', 'pathlib']),
('Chapter_12.ch12_r11', ['typing', 'pathlib']),
('Chapter_12.ch12_r12', ['typing', 'argparse'])
]

# Building a set with the add method 
all_imports = set()

for item, import_list in import_details:
    for name in import_list:
        all_imports.add(name)

print(all_imports)


all_imports = { name for item, import_list in import_details for name in import_list }
print(all_imports)


#Union Sets

collection = {1}
item = 3
collection.union({item}) # {1}
print(collection)
collection = collection.union({item}) # {1,3}
print(collection)
collection = {1}
collection = collection | {item} # {1,3}
print(collection)
collection.update({5})
print(collection) #{1, 3, 5}

# Removing items from a set – remove(), pop(), and difference

to_be_ignored = {'IP: 0.0.0.0', 'IP: 1.2.3.4'}
matches = {'IP: 111.222.111.222', 'IP: 1.2.3.4'}

print(matches - to_be_ignored )
print(matches.difference(to_be_ignored))

valid_matches = matches.copy()
for item in to_be_ignored: 
    if item in valid_matches:
        valid_matches.remove(item)
print(valid_matches) #{'IP: 111.222.111.222'}

from enum import Enum
import random

class Die(str, Enum):
    d_1 = "\u2680"
    d_2 = "\u2681"
    d_3 = "\u2682"
    d_4 = "\u2683"
    d_5 = "\u2684"
    d_6 = "\u2685"

def zonk(n: int = 6) -> Tuple[Die, ...]:
    faces = list(Die)
    return tuple(random.choice(faces) for _ in range(n))


def eval_zonk_6(hand: Tuple[Die, ...]) -> str:
    assert len(hand) == 6, "Only works for 6-dice zonk."
    unique: Set[Die] = set(hand)
    faces = list(Die)
    small_straights = [
        set(faces[:-1]), set(faces[1:])
    ]
    if len(unique) == 6:
        return "large straight"
    elif len(unique) == 5 and unique in small_straights:
        return "small straight"
    elif len(unique) == 2:
        return "three of a kind"
    elif len(unique) == 1:
        return "six of a kind!"
    elif len(unique) in {3, 4}:
        frequencies: Set[int] = set(collections.Counter(hand).values())
        if 3 in frequencies or 4 in frequencies:
            return "three of a kind"
        elif Die.d_1 in unique:
            return "ace"

    return "Zonk!"

hand: Tuple[Die, ...] = zonk()
print(hand)
print(eval_zonk_6(hand))
