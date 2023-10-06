import random
from typing import List, NamedTuple

Spades, Hearts, Diamonds, Clubs = '\u2660\u2661\u2662\u2663'


class Card(NamedTuple):

    rank: int
    suit: str

# Class design: Wrapper 
class  Deck_W():

    def __init__(self, cards: List[Card]):
        self.cards = cards
        self.deal_iter = iter(cards)

    def shuffle(self) -> None:
        random.shuffle(self.cards)
        self.deal_iter = iter(self.cards)

    def deal(self) -> Card:
        return next(self.deal_iter)


domain = list(
    Card(r + 1, s) for  r in range(13) for s in (Spades, Hearts, Diamonds, Clubs)
)

print(len(domain))


d = Deck_W(domain)
random.seed(1)
d.shuffle()
hand = [d.deal() for _ in range(5)]

for card in hand:
    print(card)

#Class design: Extending - inheritance
class Deck_X(list):


    def shuffle(self) -> None:
        random.shuffle(self)
        self.deal_iter = iter(self)

    def deal(self) -> Card:
        return next(self.deal_iter)


#d2 =  Deck_X(domain) >> Option 1 to init deck

d2 = Deck_X(
    Card(r + 1, s) for r in range(13) for s in (Spades, Hearts, Diamonds, Clubs)
)

print(len(d2))

random.seed(1)
d2.shuffle()

hand = [d2.deal() for _ in range(5)]

for card in hand:
    print(card)
