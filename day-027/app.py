"""
Exercise 85: Using the dataclass Module
"""

import dataclasses

@dataclasses.dataclass
class Point:
    x: int
    y: int


p = Point(10, 10)
p2 = Point(10, 10)
print(p == p2)
print(dataclasses.asdict(p))
