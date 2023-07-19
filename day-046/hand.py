from typing import List, Union

from Card import CardPoints


class Hand:
    __slots__= ('cards', 'bet')


    def __init__(self, bet: int, hand: Union['Hand', List[CardPoints], None] = None) -> None:
        self.bet:int = bet
        self.cards: List[CardPoints] = (
            [] if hand is None
                else hand.cards if isinstance(hand, Hand)
                    else hand
        )

    def deal(self, card: CardPoints) -> None:
        self.cards.append(card)


    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"bet={self.bet}, hand={self.cards})"
        )


h1 = Hand(2)

h1.deal(CardPoints(rank=4,suit='♡'))
h1.deal(CardPoints(rank=8, suit='♣'))

print(h1)

h1.bet *= 2

print(h1)
#h1.some_other_attribute = True # with __slots__ we can't add new attributes
