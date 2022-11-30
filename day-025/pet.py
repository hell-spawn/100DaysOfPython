"""
Exercise 74: Adding an Instance Method to Our Pet Class
"""

class Pet():
    """
    A class to capture useful information regarding my pets, just incase
    I lose track of them.
    """
    is_human: bool = False
    owner: str = 'Michael Smith'

    def __init__(self, height: int, name: str) -> None:
        self.height = height
        self.name = name

    #def is_tall(self) -> bool: 
    #    return self.height >= 50

    def is_tall(self, tall_if_at_least: int) -> bool:
        return self.height >= tall_if_at_least

    def __str__(self) -> str:
        return '%s (height: %s cm)' % (self.name, self.height)


    #@staticmethod
    #def owned_by_smith_family() -> bool:
    #    return 'Smith' in Pet.owner

    """
    Exercise 78: Extending Our Pet Class with Class Methods
    """ 

    @classmethod
    def owned_by_smith_family(cls) -> bool:
        return 'Smith' in Pet.owner



chubbles = Pet(height=5, name='chubbles')

print(type(chubbles))
print(chubbles.is_human)
print(chubbles.owner)
print(chubbles.height)
print(chubbles.__doc__)

bowser = Pet(40, 'bowser')
print(bowser.is_tall(50))
bowser.height = 60
print(bowser.is_tall(50))
print(bowser.__str__())

print(Pet.owned_by_smith_family())
nibbles = Pet(100, 'nibbles')
print(nibbles.owned_by_smith_family())


