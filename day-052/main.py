from functools import reduce

average = lambda x , y, z : (x + y + z) / 3

print(average(2, 2, 2))


concat_and_uppercase = lambda str1, str2: (f'The concatenated string {str1 + str2}'.upper())

print(concat_and_uppercase("Hello", "Lambda"))

multiply = lambda x, y: print(f'{x} * {y} = {x * y}' )
multiply(3, 2)


multiply = lambda x, y: (f'{x} * {y} = {x * y}' )
print(multiply(2, 3))

(lambda x, y: print(f'{x} * {y} = {x * y}'))(2, 10) 


# List of pairs of numbers
pairs = [(2, 3), (4, 5), (6, 7)]

# Using lambda function with map to multiply each pair and print the result
list(map(lambda pair: print(f'{pair[0]} * {pair[1]} = {pair[0] * pair[1]}'), pairs))

# List of ages
ages = [25, 30, 18, 42, 17, 50, 22, 19]

# Function to filter adults (age 18 and above) using filter with lambda
adults = filter(lambda age: age >= 18, ages)
print(list(adults))  # Output: [25, 30, 18, 42, 50, 22, 19]

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce with lambda to sum the numbers
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15

cities = ["India", "Germany", "America", "Japan"]
sorted_cities = sorted(cities, key=lambda city: city.lower())

print(sorted_cities)  # Output: ['America', 'Germany', 'India', 'Japan']

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using lambda in list comprehension to square each number
squared_numbers = [(lambda x: x ** 2)(x) for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
