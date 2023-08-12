from types import TracebackType
from typing import Callable, NamedTuple, Optional, Type
from Utils import haversine, NM, MI, KM

class Point(NamedTuple):
    lat: float
    lon: float

class Distance():

    def __init__(self, r: float) -> None:
        self.r = r

    # Init context manager 
    def __enter__(self) -> Callable[[Point, Point], float]:
        return self.distance

    # Close context manager
    def __exit__(self,
                 exc_type: Optional[Type[Exception]],
                 exc_val: Optional[Exception],
                 exc_tb: Optional[TracebackType]
                 ) -> Optional[bool]:
        return None

    def distance(self, p1: Point, p2: Point) -> float:
        return haversine(p1.lat, p1.lon, p2.lat, p2.lon, self.r)


p1 = Point(38.9784, -76.4922)
p2 = Point(36.8443, -76.2922)
# Create instance for Distans 
nm_distance = Distance(r=NM)
with nm_distance as nm_calc: # Distance return function 
    print(f"{nm_calc(p1, p2)=:.2f}") # Run function
