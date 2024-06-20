from typing import Callable

# First-Class Functions
## Assigned to variables

def add(a: int, b: int) -> int: 
    return a + b

result = add(3, 4)

print(add)             # Prints the function object
print(result)          # Prints 7

## Passed as arguments to other functions

def double(n: int) -> int:
    return n * 2

def map_function(func, values) -> list[int]:
    result: list[int] = []
    for value in values:
        result.append(func(value))
    return result

# Use the custom map function
doubled_values = map_function(double, [3, 6, 9, 12, 15])
print(doubled_values)  # Output: [6, 12, 18, 24, 30]

## Returned from other functions

def create_multiplier(factor: int) -> Callable[[int], int]:
    """Returns a function that multiplies its input by the given factor."""
    def multiplier(n: int) -> int:
        return n * factor
    return multiplier

# Create specific multiplier functions
triple_mp = create_multiplier(3)
double_mp = create_multiplier(2)


# Use the created functions
print(double_mp(5))  # Output: 10
print(triple_mp(5))  # Output: 15

def map_function(func, values) -> list[int]:
    return [func(value) for value in values]

# Using a lambda function as the argument
doubled_values = map_function(lambda n: n * 2, [3, 6, 9, 12, 15])
print(doubled_values)  # Output: [6, 12, 18, 24, 30]


def discount_applier(discount_rate: int) -> Callable[[int], float] :
    def apply_discount(price: int) -> float:
        return price - (price * discount_rate / 100)
    return apply_discount

# Creating closures with different discount rates
holiday_discount = discount_applier(20)
member_discount = discount_applier(15)

# Applying the discounts
print(holiday_discount(100))  # Output: 80.0
print(holiday_discount(200))  # Output: 160.0
print(member_discount(100))   # Output: 85.0
print(member_discount(200))   #import tkinter as tk


def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        print(f'{count} times')
    return counter

counter1 = create_counter()
counter2 = create_counter()

for _ in range(5):
    counter1()

counter2()


