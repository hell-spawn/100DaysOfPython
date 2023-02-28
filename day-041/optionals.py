import csv
from typing import Dict, Optional, TextIO
from pathlib import Path


def rtd(
        rate: Optional[float] = None,
        time: Optional[float] = None,
        distace: Optional[float] = None
        ) -> Dict[str, Optional[float]]:
    if distace is None and time is not None and rate is not None:
        distace = rate * time
    elif time is None and distace is not None and rate is not None:
        time = distace / rate
    elif rate is None and distace is not None and time is not None:
        rate = distace / time
    else:
        print("Nothing to solve for")
    return dict(distance = distace, time = time, rate = rate)

# The wind chill
def Twc(T: float, V: float) -> float:
    return 13.12 + 0.6215*T - 11.37*V**0.16 + 0.3965*T*V**0.16

"""
When we try to use the confusing positional parameters, we'll see this:
    """
def wind_chill ( start_T: int, stop_T: int, step_T: int,
        start_V: int, stop_V: int, step_V: int,
        target: TextIO) -> None:
    """Wind Chill Table."""
    writer= csv.writer(target)
    heading = ['']+[str(t) for t in range(start_T, stop_T, step_T)]

    writer.writerow(heading)
    for V in range(start_V, stop_V, step_V):
        row = [float(V)] + [ Twc(T, V) for T in range(start_T, stop_T, step_T) ]
        writer.writerow(row)


p = Path('data/wc1.csv')
with p.open('w', newline='') as target:
    #When we try to use the confusing positional parameters, we'll see this:
    wind_chill(0, -45, -5, 0, 20, 2, target)

"""
*, when used by itself The remaining parameters
can only be provided by keyword.
"""
def wind_chill_V2 ( *, start_T: int, stop_T: int, step_T: int,
        start_V: int, stop_V: int, step_V: int,
        target: TextIO) -> None:
    """Wind Chill Table."""
    writer= csv.writer(target)
    heading = ['']+[str(t) for t in range(start_T, stop_T, step_T)]

    writer.writerow(heading)
    for V in range(start_V, stop_V, step_V):
        row = [float(V)] + [ Twc(T, V) for T in range(start_T, stop_T, step_T) ]
        writer.writerow(row)


p = Path('data/wc1.csv')
with p.open('w', newline='') as output_file:
    #When we try to use the confusing positional parameters, we'll see this:
    #wind_chill_V2(0, -45, -5, 0, 20, 2, target) # Error not positional parameters
    #We must use the function with explicit parameter names, as follows:
     wind_chill(start_T=0, stop_T=-45, step_T=-5,
             start_V=0, stop_V=20, step_V=2,
             target=output_file) 
