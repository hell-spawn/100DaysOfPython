import re

title = "And now for something completely different"
pattern = "(\w)\\1+"

print(re.search(pattern, title))


description = "The Norwegian Blue is a wonderful parrot. This parrot is notable for its exquisite plumage."

pattern = "(parrot)"
replacement = "ex-\\1"

print(re.sub(pattern, replacement, description))

"""
Activity 21: Regular Expressions
"""

customers = ["Xander Harris", "Jennifer Smith", "Timothy Jones", "Amy Alexandrescu", "Peter Price", "Weifung Xu"]

pattern = "[Xx]"

winners = [winner for winner in customers if re.search(pattern, winner) ]

print(winners)
