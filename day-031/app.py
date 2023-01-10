"""
Exercise 104: The Simplest Iterator
"""

import re


class Interrogator:

    def __init__(self, questions) -> None:
        self.questions = questions

    def __iter__ (self):
        return self.questions.__iter__()



questions = ["What is your name?", "What is your quest", "What is the average airspeed velocity of an unladen swallow"]

awkward_person = Interrogator(questions)

for question in awkward_person:
    print(question)

"""
Exercise 105: A Custom Iterator
"""


class PrimesBelow:

    def __init__(self, bound) -> None:
        self.candidate_numbers= list(range(2, bound))

    
    def __iter__(self):
        return self

    def __next__(self):
        if (len(self.candidate_numbers) == 0):
            raise StopIteration
        next_prime = self.candidate_numbers[0]
        print(f"--> {next_prime}")
        self.candidate_numbers= [x for x in self.candidate_numbers if x % next_prime != 0]
        print(f"--> {self.candidate_numbers}")
        return next_prime

#primes_to_a_hundred = [prime for prime in PrimesBelow(100)]
#print(primes_to_a_hundred)


"""
Exercise 106: Controlling the Iteration
"""
primes_under_five = iter(PrimesBelow(5))

#print(next(primes_under_five))
#print(next(primes_under_five))
#print(next(primes_under_five))


"""
Exercise 107: Using Infinite Sequences and takewhile
"""
class Primes:
    def __init__(self):
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            current = self.current
            square_root = int(current ** 0.5)
            is_prime = True
            if square_root >= 2:
                for i in range(2, square_root + 1):
                    if current % i == 0:
                        is_prime = False
                        break
            self.current += 1
            if is_prime:
                return current


#print([p for p in Primes() if p < 100]) # Never print


import itertools

print([p for p in itertools.takewhile(lambda x: x<100, Primes())])

"""
Exercise 108: Turning a Finite Sequence into an Infinite One, and Back Again
"""

players = ['White', 'Black']
turns = itertools.cycle(players)
countdown = itertools.count(10, -1)

print([turn for turn in itertools.takewhile(lambda x:next(countdown) > 0, turns)])

