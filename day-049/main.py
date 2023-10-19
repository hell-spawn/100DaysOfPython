import re
from typing import Iterable, Iterator, Match, NamedTuple, cast
import datetime
import typing_extensions

'''
Writing generator functions with the yield statement
'''

log_lines: list[str] =[
        '[2016-06-15 17:57:54,715] INFO in ch10_r10: Sample Message One',
        '[2016-06-15 17:57:54,715] DEBUG in ch10_r10: Debugging',
        '[2016-06-15 17:57:54,715] WARNING in ch10_r10: Something might have gone wrong',
        ] 

class RawLog(NamedTuple):
    date: str
    level: str
    module: str
    message: str



def parse_line_iter(source: Iterable[str]) -> Iterator[RawLog]:
    pattern = re.compile(
            r"\[(?P<date>.*?)\]\s+"
            r"(?P<level>\w+)\s+"
            r"in\s+(?P<module>.+?)"
            r":\s+(?P<message>.+)",
            re.X)
    for line in source:
        if match := pattern.match(line):
            yield RawLog(**match.groupdict())


#for log in parse_line_iter(log_lines):
#    print(log)

class DatedLog(NamedTuple):

    date: datetime.datetime
    level: str
    module: str
    message: str

def parse_date_iter( source: Iterable[RawLog]) -> Iterator[DatedLog]: 
    for item in source:
        date: datetime.datetime = datetime.datetime.strptime( item.date, "%Y-%m-%d %H:%M:%S,%f")
        yield DatedLog( date, item.level, item.module, item.message)


for log in parse_date_iter(parse_line_iter(log_lines)):
    print(log)
