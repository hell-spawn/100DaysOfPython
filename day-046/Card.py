from typing import NamedTuple

"""
Inmutable class
"""
class CardPoints(NamedTuple):

    rank: int
    suit: str

    def points(self) -> int:
        if 1 <= self.rank < 10:
            return self.rank
        else:
            return 10

eight_card = CardPoints(8, '\N{White Heart Suit}')

print(eight_card)
print(eight_card.points())

from dataclasses import dataclass
from typing import List

@dataclass
class CribbageHand:

    cards: List[CardPoints]

    def to_crib(self, card1, card2):
        self.cards.remove(card1)
        self.cards.remove(card2)



cards = [ CardPoints(rank=3, suit='◊'),
        CardPoints(rank=6, suit='♠'),
        CardPoints(rank=7, suit='◊'),
        CardPoints(rank=1, suit='♠'),
        CardPoints(rank=6, suit='◊'),
        CardPoints(rank=10,suit='♡') ]


cribbageHand = CribbageHand(cards)


print(cribbageHand.__repr__())

result = [c.points() for c in cribbageHand.cards]
print(result)

cribbageHand.to_crib(CardPoints(rank=3, suit='◊'), CardPoints(rank=1, suit='♠'))

print(cribbageHand.__repr__())
result = [c.points() for c in cribbageHand.cards]
print(result)
