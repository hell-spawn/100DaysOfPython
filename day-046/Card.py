from typing import NamedTuple

"""
Immutable class
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
print(eight_card.rank) #Attributes for name
print(eight_card[0]) #Attributes for position
print(eight_card.points())


#eight_card.suit = '\N{Black Spade Suit}' # Error attribute static

from dataclasses import dataclass
from typing import List

## Dataclass create basic methods to tha class
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

