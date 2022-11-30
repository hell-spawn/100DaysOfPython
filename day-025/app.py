import math


"""
Exercise 72, Creating a Circle Class:
"""
class Circle():

    is_shape: bool = True

    #def __init__(self, radius: int, color: str) -> None: 
    def __init__(self, radius: int, color: str = 'Red') -> None:
        self.radius = radius
        self.color = color
    
    def area(self) -> float:
        return math.pi * self.radius ** 2


first_circle = Circle(2, 'blue')
second_circle = Circle(3, 'red')
third_circle = Circle(4)

print(first_circle.color)
print(second_circle.color)
print(third_circle.color)

print(first_circle.area())
first_circle.is_shape = False
print(first_circle.is_shape)
print(second_circle.is_shape)


class Pet():
    """
    A class to capture useful information regarding my pets, just incase
    I lose track of them.
    """
    is_human = False
    owner = 'Michael Smith'
    def __init__(self, height):
        self.height = height

chubbles = Pet(height=5)

print(type(chubbles))
print(chubbles.is_human)
print(chubbles.owner)
print(chubbles.height)
print(chubbles.__doc__)


class Country():
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

usa = Country(name='United States of America', size_kmsq=9.8e6)

print(usa.__dict__)
