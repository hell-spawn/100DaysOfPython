from typing import Tuple, List, DefaultDict, Iterable, Iterator
import collections
import re

log = """[2019/11/12:08:09:10,123] INFO #PJQXB^eRwnEGG?2%32U path="/openapi.yaml" method=GET
[2019/11/12:08:09:10,234] INFO 9DiC!B^nXxnEGG?2%32U path="/items?limit=x" method=GET
[2019/11/12:08:09:10,235] INFO 9DiC!B^nXxnEGG?2%32U error="invalid query"
[2019/11/12:08:09:10,345] INFO #PJQXB^eRwnEGG?2%32U status="200" bytes="11234"
[2019/11/12:08:09:10,456] INFO 9DiC!B^nXxnEGG?2%32U status="404" bytes="987"
[2019/11/12:08:09:10,567] INFO >UL>PB_R>&nEGG?2%32U path="/category/42" method=GET"""

log_parser = re.compile(r"\[(.*?)\] (\w+) (\S+) (.*)")

# Creating dictionaries – inserting and updating
# Build Dictioaries Literal
litera_dict = {"num": 35, "text": "some_text" }
print(litera_dict)

# Build Dictioaries conversion
conversion_dict = dict([("num", 35), ("text", "some_text")])
print(conversion_dict)

# Build Dictioaries compreshesion
param_parser = re.compile(r'(\w+)=(".*?"|\w+)')
for line in log.split('\n'):
    name_value_pairs = param_parser.findall(line)
    params = { match[0]: match[1] for match in name_value_pairs }
    print(params)

# Removing items from dictionaries – the pop() method and the del statement
log_parser = re.compile(r"\[(.*?)\] (\w+) (\S+) (.*)")
LogRec = Tuple[str, ...]

log = """[2019/11/12:08:09:10,123] INFO #PJQXB^eRwnEGG?2%32U path="/openapi.yaml" method=GET
[2019/11/12:08:09:10,234] INFO 9DiC!B^nXxnEGG?2%32U path="/items?limit=x" method=GET
[2019/11/12:08:09:10,235] INFO 9DiC!B^nXxnEGG?2%32U error="invalid query" 
[2019/11/12:08:09:10,345] INFO #PJQXB^eRwnEGG?2%32U status="200" bytes="11234"
[2019/11/12:08:09:10,456] INFO 9DiC!B^nXxnEGG?2%32U status="404" bytes="987"
[2019/11/12:08:09:10,567] INFO >UL>PB_R>&nEGG?2%32U path="/category/42" method=GET"""


def request_iter_t(source: Iterable[str]) -> Iterator[List[LogRec]]: 
    requests: DefaultDict[str, List[LogRec]] = collections.defaultdict(list)
    for line in source:
        if match := log_parser.match(line):
            id = match.group(2)
            requests[id].append(tuple(match.groups()))
            if match.group(4).startswith('status'):
                yield requests[id]
                del requests[id]
    if requests:
        print("Dangling", requests)



print("--------------------------------")
for r in request_iter_t(log.splitlines()):
    print(r)



# Controlling the order of dictionary keys
import csv
from pathlib import Path
from typing import List, Dict
def get_fuel_use(source_path: Path) -> List[Dict[str, str]]:
    with source_path.open() as source_file:
        rdr= csv.DictReader(source_file)
        data: List[Dict[str, str]] = list(rdr)
    return data

print("--------------------------------")
source_path = Path("../data/fuel2.csv")
fuel_use = get_fuel_use(source_path)
key_order = [ "date","engine on","engine off","fuel height on", "fuel height off" ]
for row in fuel_use:
    print(row)
    row = collections.OrderedDict([(name, row[name]) for name in key_order])
    print(dict(row))

# Writing dictionary-related type hints

from typing import TypedDict
import datetime 


History = TypedDict( 
        'History', { 
            'date': datetime.date,
            'start_time': datetime.time,
            'start_fuel': float,
            'end_time': datetime.time,
            'end_fuel': float
            }
        )

def make_history(source: Iterable[Dict[str, str]]) -> Iterator[History]:
    for row in source:
        yield History(
                date = datetime.datetime.strptime(row['date'], "%m/%d/%y").date(),
                start_time = datetime.datetime.strptime(row['engine on'], '%H:%M:%S').time(),
                start_fuel = float(row['fuel height on']),
                end_time = datetime.datetime.strptime(row['engine off'], '%H:%M:%S').time(),
                end_fuel = float(row['fuel height off']),
                )
print("--------------------------------")
source_path = Path("../data/fuel2.csv")
fuel_use = make_history(get_fuel_use(source_path))
for row in fuel_use: 
    print(row)

from typing import NamedTuple

HistoryT = NamedTuple(
        'HistoryT', [ 
            ('date', datetime.date),
            ('start_time', datetime.time),
            ('start_fuel', float),
            ('end_time', datetime.time),
            ('end_fuel', float)
            ]
        )

def make_history_t(source: Iterable[Dict[str, str]]) -> Iterator[HistoryT]:
    for row in source:
        yield HistoryT(
                date = datetime.datetime.strptime(row['date'], "%m/%d/%y").date(),
                start_time = datetime.datetime.strptime(row['engine on'], '%H:%M:%S').time(),
                start_fuel = float(row['fuel height on']),
                end_time = datetime.datetime.strptime(row['engine off'], '%H:%M:%S').time(),
                end_fuel = float(row['fuel height off']),
                )
print("--------------------------------")
source_path = Path("../data/fuel2.csv")
fuel_use = make_history(get_fuel_use(source_path))
for row in fuel_use: 
    print(row)


# Understanding variables, references, and assignment
# Making shallow and deep copies of objects
# Avoiding mutable default values for function parameters
