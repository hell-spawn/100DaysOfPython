import random
from typing import Iterable, Iterator, Tuple
from random import randint


class Dice():

    """
    Docstring for Dice.
    """

    def __init__(self) -> None:
        """Constructs all the necessary attributes for the Dice object. """
        self.faces: Tuple[int, int] = (0, 0)


    def roll(self) -> None:
        self.faces = (randint(1,6), randint(1,6))


    def total(self) -> int:
        return sum(self.faces)

    def hardway(self) -> bool:
        return self.faces[0] == self.faces[1]

    def easyway(self) -> bool:
        return self.faces[0] != self.faces[1]

#random.seed(1)
#
#d1 = Dice()
#d1.roll()
#print(d1.total())
#print(d1.faces)
#
#d2 = Dice()
#d2.roll()
#print(d2.total())
#print(d2.faces)
#print(d2.hardway())
#

def coupon_collector(n: int, data: Iterable[int]) -> Iterator[int]:
    """
    >>> samples = [0, 1, 2, 3, 0, 0, 1, 1, 2, 2, 3, 3]
    >>> list(coupon_collector(4, samples))
    [4, 7]
    """
    count, collection = 0, set()
    for item in data:
        count += 1
        # collection = collection|{item}
        collection.add(item)
        print(f'Count: {count}')
        print(f'Collection: {collection}')
        if len(collection) == n:
            yield count
            count, collection = 0, set()


samples = [0, 1, 2, 3, 0, 0, 1, 1, 2, 2, 3, 3]
print(list(coupon_collector(4, samples)))
