import random
import re
from typing import Literal, LiteralString


NUM_DIGITS = 3
MAX_GUESSES = 10

def main() -> None:
    print("Bagles")

    while True:
        print(f"Bagles! I am thinking of a {NUM_DIGITS} digit number. Try to guess what it is.")
        print("The clues I give are:")
        print("PICO   - One digit is correct but in the wrong position")
        print("FERMI  - One digit is correct and in the right position")
        print("BAGELS - No digits is correct") 
        secretNum = getSecretNumber() 
        print(secretNum)
        maxAttempts = 1; 

       
        while maxAttempts <= MAX_GUESSES:
            print(f"Guess #{maxAttempts}: ")
            guess = input('> ')
            result = getClues(secretNum, guess)

            if secretNum == guess:
                print("You won, Nice job!!!");
                break
            
            print(result)
            maxAttempts += 1

            if maxAttempts > MAX_GUESSES:
                print("You ran out attempts")
                print(f"The correct answers is: {secretNum}")

        play_again = input("Do you want again (y/n): ")

        if play_again != 'y':
            break
        
        

def getSecretNumber() -> str:
    NUMBERS = list('1234567890')
    random.shuffle(NUMBERS)
    
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(NUMBERS[i])
    return secretNum 

def getClues(secretNum: str, guess: str) -> (LiteralString | str):
    
    clues = []
    for i in range(NUM_DIGITS):
        if guess[i] == secretNum[i]:
            clues.append("FERMI")
            continue

        if guess[i] in secretNum:
            clues.append("PICO")
            continue
       
    if len(clues) == 0:
        return "Bagles"

    clues.sort()
    return ' '.join(clues)

if __name__ == '__main__':
    main()

        
        

