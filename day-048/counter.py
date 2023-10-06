import collections

from typing import List, Tuple, Any, Counter
from dice import Dice1

# Module global is singleton instance

_global_counter: Counter[str] = collections.Counter()


def count(key: str, increment: int = 1) -> None:
    _global_counter[key] += increment 


def count_summary() -> List[Tuple[str, int]]:
    return _global_counter.most_common() 



d:Dice1 = Dice1()

for _ in range(1000):
    if sum(d.roll()) == 7: count('seven') 
    else: count('other')

print(count_summary())


class EvenCounter:

    _class_counter: Counter[str] = collections.Counter()

    def count(self, key: str, increment: int = 1) -> None:
        EvenCounter._class_counter[key] += increment


    def count_summary(self) -> List[Tuple[str, int]]:
        return EvenCounter._class_counter.most_common()

   
for _ in range(1000):
    if sum(d.roll()) == 7: EvenCounter().count('seven') 
    else: EvenCounter().count('other')

print(EvenCounter().count_summary())



