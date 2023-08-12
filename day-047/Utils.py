"""Python Cookbook 2nd ed.

Chapter 3, Recipe 8, Picking an order for parameters based on partial functions
"""
from math import radians, sin, cos, sqrt, asin
from typing import Callable

MI = 3959
NM = 3440
KM = 6373


def haversine( lat_1: float, lon_1: float, lat_2: float, lon_2: float, R: float = NM) -> float:
    """Distance between points.

    R is radius, R=MI computes in miles. Default is nautical miles.

    >>> round(haversine(36.12, -86.67, 33.94, -118.40, R=6372.8), 5)
    2887.25995
    """
    Δ_lat = radians(lat_2) - radians(lat_1)
    Δ_lon = radians(lon_2) - radians(lon_1)
    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)

    a = sqrt(sin(Δ_lat / 2) ** 2 + cos(lat_1) * cos(lat_2) * sin(Δ_lon / 2) ** 2)

    return R * 2 * asin(a)












