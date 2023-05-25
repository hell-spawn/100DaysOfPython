from pathlib import Path
import csv
from typing import Dict, List


def get_fuel_use(source_path: Path) -> List[Dict[str, str]]:
    with source_path.open() as source_file:
        rdr = csv.DictReader(source_file)
        return list(rdr)

source_path = Path("../data/fuel2.csv")
fuel_use = get_fuel_use(source_path)
#Simple Print
for row in fuel_use:
    print(row)
print("------------------------------")
for leg in fuel_use:
    start = float(leg["fuel height on"])
    finish = float(leg["fuel height off"])
    print("On", leg["date"], "from", leg["engine on"], "to", leg["engine off"], "change", start-finish, "in.")

print("------------------------------")
for leg in fuel_use:
    start = float(leg["fuel height on"])
    finish = float(leg["fuel height off"])
    print("On", leg["date"], "from", leg["engine on"], "to", leg["engine off"], "change", start-finish, "in.")

print("------------------------------")
print("date", "start", "end", "depth", sep=" | ")
for leg in fuel_use:
    start = float(leg["fuel height on"])
    finish = float(leg["fuel height off"])
    print(leg["date"], leg["engine on"], leg["engine off"], start-finish, sep=" | ") 


print("------------------------------")
for leg in fuel_use:
    start = float(leg["fuel height on"])
    finish = float(leg["fuel height off"])
    print("date", leg["date"], sep="=", end=", ")
    print("on", leg["engine on"], sep="=", end=", ")
    print("off", leg["engine off"], sep="=", end=", ")
    print("change", start-finish, sep="=")

print("------------------------------")
from datetime import date
def get_date1() -> date:
    year = int(input("year: "))
    month = int(input("month [1-12]: "))
    day = int(input("day [1-31]: "))
    result = date(year, month, day)
    return result


#print( get_date1() )

print("------------------------------")
import statistics
size = [2353, 2889, 2195, 3094, 725, 1099, 690, 1207, 926, 758, 615, 521, 1320]
mean_size = statistics.mean(size)
std_size = statistics.stdev(size)
sig1 = round(mean_size + std_size, 1)

print( 
        f"{mean_size=:.2f}, {std_size=:.2f},"
        f" {mean_size+2*std_size=:.2f}"
        )

print ([x for x in size if x > sig1])
