from operator import ge
from pathlib import Path
from re import I


# Ways to creat a list:
# Listeral: [item, item,...]
# Conversion function list()
# Append method months  = [] months.append('Ene')
# Commprehension
# Generator expresion


home = Path.cwd()
home = home.parent
append_list = []
for path in home.glob('data/*.csv'):
    print(path.stat().st_size, path.name)
    append_list.append(path.stat().st_size)

print(append_list)
print(sum(append_list))

commprehension_list = [path.stat().st_size for path in home.glob('data/*.csv')]

print(commprehension_list)
print(sum(commprehension_list))

generator_list = list(path.stat().st_size for path in home.glob('data/*.csv'))

print(generator_list)
print(sum(generator_list))

# Example use Dictionary
scheme = {
        "Crimson": (220, 14, 60), 
        "DarkCyan": (0, 139, 139), 
        "Yellow": (255, 255, 00)
        }
print(scheme['Crimson']) # (220, 14, 60)


# Ways to creat a list:
# Listeral: [item, item,...]
# Conversion function list()
# Append method months  = [] months.append('Ene')
# Commprehension
# Generator expresion

#Example use List
month_name_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print(month_name_list[8]) # 'Sep'
print(month_name_list.index("Feb")) # 1
# print(month_name_list[13]) # IndexError: list index out of range
# print(month_name_list.index("Mon")) # ValueError: 'Mon' is not in lis ValueError: 'Mon' is not in listt 


# Set Each item in set must be an immutable ex. Numbers, String and tuples
# Example use set
def confirm() -> bool:
    yes = {"yes", "y"}
    no = {"no", "n"}
    # Union sets
    valid_inputs = (yes | no)
    # We can't add another y to a set that already contains y.
    valid_inputs.add("y") # {'y', 'no', 'n', 'yes'}
    while (answer := input("Confirm: ")).lower() not in valid_inputs:
        print("please respond yes or no")
    return answer in yes


print(confirm())

        
