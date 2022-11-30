"""
Exercise 75: Computing the Size of Our Country
Exercise 76: Adding an __str__ Method to the Country Class
"""
from typing import Optional


class Country():

    def __init__(self, name: str='Unspecified', population: Optional[int]=None, size_kmsq: Optional[float] =None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def size_miles_sq(self, conversion_rate: float=0.621371) -> float:
        if(self.size_kmsq):
            return self.size_kmsq * conversion_rate ** 2
        return 0.0


    def __str__(self) -> str:
        return '{name: "%s" }' % (self.name)


    @classmethod
    def create_with_msq(cls, name, population, size_msq):
        size_kmsq = size_msq / 0.621371 ** 2
        return cls(name, population, size_kmsq)

usa = Country(name='United States of America', size_kmsq=9.8e6)
algeria = Country(name='Algeria', size_kmsq=2.382e6)
print(usa.__dict__)
print(algeria.size_miles_sq())

print(usa.__str__())

mexico = Country.create_with_msq('Mexico', 150e6, 760000)
print(mexico.size_kmsq)
