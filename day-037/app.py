import re
import os

"""Regular Expresions"""

ingredient = "Kumquat: 2 cups"

# Separete ingredient from measurements

ingredient_pattern = re.compile(r'([\w\s]+):\s+(\d+)\s+(\w+)')

mathers = ingredient_pattern.match(ingredient)

groups = mathers.groups()

print(groups)

"""Complex strings with f-string"""

id = "IAD"
location = "Dulles Intl Airport"
max_temp = 32
min_temp = 13
precipitation = 0.4

print(f'{id} : {location} : {max_temp} / {min_temp} / {precipitation}')

print(f'{id:s} : {location:s} : {max_temp:d} / {min_temp:d} / {precipitation:f}') #  The basic data type

print(f'{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}') # Length information

data = dict( id=id, location=location, max_temp=max_temp, min_temp=min_temp, precipitation=precipitation)

print('{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format_map(data)) # f-strings format 

print('You Rolled \u2680') # Unicode Caracter  
print('You skull ' + '\u2620') #
print('Discard \N{MAHJONG TILE RED DRAGON}') # 

# set python encode export PYTHONIOENCODING=UTF-8
print(os.environ.get('PYTHONIOENCODING', '').lower()) 

with open('some_file.txt', 'w', encoding='utf-8') as output:
    print( 'You drew \U0001F000', file=output )

with open('some_file.txt', 'r', encoding='utf-8') as input:
    text = input.read()
    print(text)


string_bytes = 'You drew \U0001F000'.encode('utf-8') # Set manual encoding

print(string_bytes)

print('You drew \U0001F000'.encode('ascii')) # Error encode

