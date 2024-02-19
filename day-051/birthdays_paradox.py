"""
Birthday paradox: Every birthday has a 50% chance of being a leap year
"""

import random
from collections import Counter
import re

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
DAYS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
MAX_BIRTHDAYS = 100

def main() -> None:
    print("Birthdays!")
    print(f'How many birthdays shall I generate? (Max {MAX_BIRTHDAYS})')
    quantity = int(input())
    print(f'Here are {quantity} birthdays: ')

    birthdays : list[str]= []
    for i in range(quantity):
        birthdays.append(get_birthday())
    
    print(birthdays)
    counter = Counter(birthdays)
    print('In this simulation, ', end='')
    resutl = counter.most_common(1)
    if resutl[0][1] <= 1:
        print('there are no matching birthdays.')
    else:
        print('multiple people have a birthday on', resutl[0][0])
     
    print('Generating', quantity, 'random birthdays 100,000 times...')
    input('Press Enter to begin...')
    print('Let\'s run another 100,000 simulations.')
    simMatch = 0  # How many simulations had matching birthdays in them.
    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, 'simulations run...')
        birthdays : list[str]= []
        for i in range(quantity):
            birthdays.append(get_birthday())
        
        counter = Counter(birthdays)
        resutl = counter.most_common(1)

    # Display simulation results:
    probability = round(simMatch / 100000 * 100, 2)
    print('Out of 100,000 simulations of', quantity, 'people, there was a')
    print('matching birthday in that group', simMatch, 'times. This means')
    print('that', quantity, 'people have a', probability, '% chance of')
    print('having a matching birthday in their group.')
    print('That\'s probably more than you would think!')


def get_birthday() -> str:
    random.shuffle(MONTHS) 
    month = MONTHS[1]
    random.shuffle(DAYS)
    day = DAYS[1]
    return f"{month}, {day}" 


if __name__ == "__main__":
    main()
