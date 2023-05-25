import collections
import math
from typing import Callable, Counter, Iterator
from collector import ( samples, arrival1, coupon_collector)
import random

class CounterStatistics:

    """
    Docstring for CounterStatistics. 
    """

    def __init__(self, raw_counter: Counter[int]) -> None:
        """Constructs all the necessary attributes for the CounterStatistics object. """
        self.raw_counter = raw_counter
        self.mean = self.compute_mean()
        self.stddev = self.compute_stddev() 

    def compute_mean(self) -> float:
        total, count = 0.0, 0
        for value, frequency in self.raw_counter.items():
            total += value * frequency
            count += frequency
        return total / count

    def compute_stddev(self) -> float:
        total, count = 0.0, 0
        for value, frequency in self.raw_counter.items():
            total += frequency * (value - self.mean) ** 2
            print(f'Value: {value}, Frequency:{frequency}, Total: {total}')
            count += frequency
        return math.sqrt(total / (count - 1))

ArrivalF = Callable[[int], Iterator[int]]

def raw_data( n: int = 8, limit: int = 1000, arrival_function: ArrivalF = arrival1) -> Counter[int]:
    data = samples(limit, arrival_function(n))
    wait_times = collections.Counter(coupon_collector(n, data))
    return wait_times

random.seed(1)

data = raw_data()
stats = CounterStatistics(data)
print("Mean: {0:.2f}".format(stats.mean))
print("Standard Deviation: {0:.3f}".format(stats.stddev))
