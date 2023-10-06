from abc import abstractmethod
import random
from typing import Iterator, Optional, Tuple, Type

class GenericDice:

    def __init__(self, seed: int) -> None:
        pass
    
    @abstractmethod
    def roll(self) -> Tuple[int, ...]:
        pass

class Dice1(GenericDice):

    def __init__(self, seed=None) -> None:
        self._rng = random.Random(seed)
        self.roll()

    def roll(self) -> Tuple[int, ...]:
        self.dice = (
                self._rng.randint(1, 6),
                self._rng.randint(1, 6)
                )

        return self.dice

class Die:

    def __init__(self, rng: random.Random) -> None:
        self._rng = rng

    def roll(self) -> int:
        return self._rng.randint(1, 6)

class Dice2(GenericDice):

    def __init__(self, seed: Optional[int] = None ) -> None:
        self._rng = random.Random(seed)
        self._dice = [Die(self._rng) for _ in range(2)]

    def roll(self) -> Tuple[int, ...]:
        dice = tuple(d.roll() for d in self._dice)
        return dice


def roller(
        dice_class: Type[GenericDice],
        seed: int, *, samples: int = 10
        ) -> Iterator[Tuple[int, ...]]:
    dice = dice_class(seed)
    for _ in range( samples ):
        yield dice.roll()

