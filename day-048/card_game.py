from dataclasses import dataclass
import random
from typing import List

Spades, Hearts, Diamonds, Clubs = '\u2660\u2661\u2662\u2663'

SUITS = [Spades, Hearts, Diamonds, Clubs]


@dataclass(frozen=True)
class Card:
    rank: int
    suit: str

    def __str__(self) -> str:
        return f"{self.rank:2d}, {self.suit}"


class AceCard(Card):

    def __str__(self) -> str:
        return f" A {self.suit}"


class FaceCard(Card):

    def __str__(self) -> str:
        names = {11: "J", 12: "Q", 13: "K"}
        return f" {names[self.rank]} {self.suit}"


@dataclass(frozen=True)
class PointedCard:
    rank: int


class CribbagePoints(PointedCard):

    def points(self: PointedCard) -> int:
        return self.rank


class CribbageFacePoints(PointedCard):

    def points(self: PointedCard) -> int:
        return 10


class CribbageCard(Card, CribbagePoints):
    pass


class CribbageAce(AceCard, CribbagePoints):
    pass


class CribbageFace(FaceCard, CribbageFacePoints):
    pass


def make_cribbage_card(rank: int, suit: str) -> Card:
    if rank == 1:
        return CribbageAce(rank, suit)
    if 2 <= rank < 11:
        return CribbageCard(rank, suit)
    if 11 <= rank:
        return CribbageFace(rank, suit)
    raise ValueError(f"Invalid rank {rank}")


random.seed(1)
deck: List[Card] = [make_cribbage_card(
    rank + 1, suit) for rank in range(13) for suit in SUITS]

random.shuffle(deck)
len(deck)

hand = [str(card) for card in deck[:5]]

print(hand)

points = sum(
    c.points() if isinstance(c, (CribbagePoints | CribbageFacePoints)) else 0 for c in deck[:5]
)

print(points)

c = deck[5]

print( c.__class__.__name__ )

# Method Resolution Order (MRO).
print(c.__class__.mro())
