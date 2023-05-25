import random
from fractions import Fraction
from statistics import mean
from typing import Iterator, Iterable, Callable, cast


def arrival1(n: int = 8) -> Iterator[int]:
    while True:
        yield random.randrange(n)




def arrival2(n: int = 8) -> Iterator[int]:
    p = 0
    while True:
        step = random.choice([-1, 0, +1])
        p += step
        yield abs(p) % n



def samples(limit: int, generator: Iterable[int]):
    for n, value in enumerate(generator):
        if n == limit:
            break
        yield value



# Interesting quirk: sum() definition doesn't properly include Fraction
def expected(n: int = 8) -> Fraction:
    return n * cast(Fraction, sum(Fraction(1, i + 1) for i in range(n)))



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
        if len(collection) == n:
            yield count
            count, collection = 0, set()


def summary( n: int, limit: int, arrival_function: Callable[[int], Iterable[int]]) -> None:
    expected_time = float(expected(n))

    data = samples(limit, arrival_function(n))
    wait_times = list(coupon_collector(n, data))
    average_time = mean(wait_times)
    print(f"Coupon collection, n={n}")
    print(f"Arrivals per {arrival_function.__name__!r}")
    print(f"Expected = {expected_time:.2f}")
    print(f"Actual {average_time:.2f}")

