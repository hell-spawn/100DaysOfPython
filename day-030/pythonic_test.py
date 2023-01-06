

cubes = []

for x in [1, 2, 3, 4, 5]:
    cubes.append( x**3 )

print(cubes)

cubes = [x**3 for x in [1, 2, 3, 4, 5]] # Collection
print(cubes)

cubes = [x**3 for x in range(1,6)] # Range
print(cubes)

print("--------------------")

names = ["Graham Chapman", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]
print([f"{x}" for x in names if x.startswith("T")])

print([x*y for x in ['spam', 'eggs', 'chips'] for y in [1,2,3]])

numbers = [1,2,3]
print([x**y for x in numbers for y in numbers])

print("--------------------")

# Set comprehesion

print([a + b for a in [0,1,2,3] for b in [4,3,2,1]]) # Collection
print({a + b for a in [0,1,2,3] for b in [4,3,2,1]}) # Set

print("--------------------")

print({k:len(k) for k in ["Eric", "Graham", "Terry", "John", "Terry"]}) # Dictionary

print("--------------------")


names = ["Magnus Carlsen", "Fabiano Caruana", "Yifan Hou", "Wenjun Ju"]
fixtures = [f"{p1} vs. {p2}" for p1 in names for p2 in names if p1 != p2] # List comprehesion 
print(fixtures)


"""
Activity 19: Building a Scorecard Using Dictionary Comprehensions and
Multiple Lists
"""

students = ["Vivian", "Rachel", "Tom", "Adrian"]
points = [70, 82, 80, 79]

scores = { students[i]:points[i] for i in range(4) } # Dictionary comprehesion

print(scores)


"""
Activity 20: Using Random Numbers to Find the Value of Pi
"""

