"""
Function parameters and type hints
"""
from typing import Tuple, Union


#Function without any hint

def hex2rgb_not_hits(hx_int):
    if(isinstance(hx_int, str)):
        if hx_int[0] == "#":
            hx_int = int( hx_int[:1], 16 )
        else:
            hx_int = int(hx_int, 16)

    r,g,b = (hx_int >> 16) & 0xFF, (hx_int >> 8) & 0xFF, (hx_int >> 0) & 0xFF
    return r, g, b


def hex2rgb(hx_int: Union[int, str]) -> Tuple[int, int, int]:
    if(isinstance(hx_int, str)):
        if hx_int[0] == "#":
            hx_int = int( hx_int[:1], 16 )
        else:
            hx_int = int(hx_int, 16)
    r,g,b = (hx_int >> 16) & 0xFF, (hx_int >> 8) & 0xFF, (hx_int >> 0) & 0xFF
    return r, g, b
