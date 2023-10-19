import re
from typing import NamedTuple, Optional, cast


date: str = '''
[2016-04-24 11:05:01,462] INFO in module1: Sample Message One
[2016-04-24 11:06:02,624] DEBUG in module2: Debugging
[2016-04-24 11:07:03,246] WARNING in module1: Something might have gone wrong
'''


class Event(NamedTuple):

    timestamp: str
    level: str
    module: str
    message: str


    @staticmethod
    def from_line(line: str) -> Optional['Event']:
        pattern = re.compile(
                r"\[(?P<timestamp>.*?)\]\s+"
                r"(?P<level>\w+)\s+"
                r"in\s+(?P<module>\w+)"
                r":\s+(?P<message>\w+)"
                )
        if log_line := pattern.match(line):
            return Event(
                    **cast(re.Match, log_line).groupdict()
                    )
        return None
        

print( Event.from_line("[2016-04-24 11:05:01,462] INFO in module1: Sample Message One"))
