"""
Collections advanced
"""

import urllib.request
import collections

# Chain 
_defaults = {
    "apetisers": "Hummus",
    "main": "Pizza",
    "dessert": "Chocolate cake",
    "drink": "Water",
}

def prepare_menu(customizations):
    return collections.ChainMap(customizations, _defaults)

def print_menu(menu):
    for key, value in menu.items():
        print(f"As {key}: {value}.")

menu1 = prepare_menu({})
print_menu(menu1)

menu3 = prepare_menu({"side": "French fries"})
print_menu(menu3)

menu2 = prepare_menu({"drink": "Red Wine"})
print_menu(menu2)

_defaults["main"] = "Pasta"
print_menu(menu3)



print('--------------------')

"""
Exercise 96: Refactoring Code with defaultdict
"""

# Original code
#_audit = {}
#def add_audit(area, action):
#    if area in _audit:
#        _audit[area].append(action)
#    else:
#        _audit[area] = [action]
# 
#def report_audit():
#    for area, actions in _audit.items():
#        print(f"{area} audit:")
#        for action in actions:
#            print(f"- {action}")
#            print()


_audit = collections.defaultdict(list)
def add_audit(area, action):
    _audit[area].append(action)
 
def report_audit():
    for area, actions in _audit.items():
        print(f"{area} audit:")
        for action in actions:
            print(f"- {action}")
            print()

add_audit("HR", "Hired Sam")
add_audit("Finance", "Used 1000£")
add_audit("HR", "Hired Tom")
report_audit()

print('--------------------')


"""
Exercise 95: Counting Words in a Text Document
"""

url = 'https://www.w3.org/TR/2003/REC-PNG-20031110/iso_8859-1.txt'
response = urllib.request.urlopen(url)
words = response.read().decode().split()
len(words) # 858

print(len(words))

word_counter = collections.Counter(words)

for word, count in word_counter.most_common(5):
    print(word, ' - ', count)

print("QUESTION", "-", word_counter["QUESTION"])
print("CIRCUMFLEX", "-", word_counter["CIRCUMFLEX"])
print("DIGIT", "-", word_counter["DIGIT"])
print("PYTHON", "-", word_counter["PYTHON"])


d = {}
def function(x):
    if x not in d:
        d[x] = 0 # or any other initialization
    else:
        d[x] += 1 # or any other manipulation

d = {}
def function(x):
    try:
        d[x] += 1
    except KeyError:
        d[x] = 1
