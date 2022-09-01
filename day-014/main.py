# 1. Import Logo,
# 2. Load Data
# 3. Random options
# 4. check answer
# 5. Increment score
# 6. show result
#
#
#
#
#
#
import os
import random

from art import logo, vs
from data_game import data


def clear(): return os.system('cls||clear')


def show_logo():
    print(logo)


def check_answer(current_character, challenger_character, answer):
    if answer == "A":
        if (current_character['follower_count'] > challenger_character['follower_count']):
            return 1
        else:
            return 0
    else:
        if (current_character['follower_count'] < challenger_character['follower_count']):
            return 1
        else:
            return 0


def game():
    current_character = None
    challenger_character = None
    isLoser = False
    score = 0
    answer = None
    while not isLoser:
        show_logo()

        if not current_character:
            current_character = random.choice(data)
            print(
                f"Compare A: {current_character['name']}, {current_character['description']}, {current_character['country']}")
        else:
            if answer == "B":
                current_character = challenger_character

            print(f"You're right! Current score: {score}.")
            print(f"Compare A: {current_character['name']}, {current_character['description']}, {current_character['country']}")

        challenger_character = random.choice(data)
        print(vs)
        print(f"Against B: {challenger_character['name']}, {challenger_character['description']}, {challenger_character['country']}")
        answer = input("Who has more followears? Type 'A' or 'B': ")
        result = check_answer(current_character, challenger_character, answer)
        if result == 0:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            isLoser = True
        else:
            score += result
            clear()


game()
