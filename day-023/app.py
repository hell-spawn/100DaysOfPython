import math

"""
Sorting with Lambda Functions
"""
names = ['Ming', 'Jennifer', 'Andrew', 'Boris']

print(sorted(names, key=lambda x : len(x)))

"""
Exercise 57: Using the Filter Lambda
"""

nums = list(range(1000))

nums_filtered = list(filter(lambda x: x % 3 == 0 or x % 7 == 0, nums))

print(sum(nums_filtered))



"""
Filtering with Lambda Functions
"""

names = ['Karen', 'Jim', 'Kim']

names = list(filter(lambda x: len(x) == 3 , names))
print(names)

"""
Exercise 56: Mapping with a Logistic Transform
"""
nums = [-3, -5, 1, 4]

result = list(map(lambda x : 1 /(1 + math.exp(-x)), nums)) 
print(result)

"""
Mapping with Lambda Functions
"""
names = ['Magda', 'Jose', 'Anne']


#Simple option
lengths = []
for name in names:
    lengths.append(len(name))

print(lengths)

#Lambda Option
lengths = list(map(len, names))

print(lengths)

"""
Exercise 55: The First Item in a List
"""

first_item = lambda my_list: my_list[0]
item = first_item(['cat', 'dog', 'mouse'])
print(item)


"""
Lambda functions
"""
# Simple function 
def add_up_simple(x, y):
    return x + y

print(add_up_simple(2, 5))

# Lambda function

add_up_lambda = lambda x,y: x +y

print(add_up_lambda(2, 5))

"""
nonlocal keyword
"""
x = 4
def myfunc():
    x = 3
    def inner():
        nonlocal x
        x = 5
        print(x)
    inner()
    print(x)
myfunc()

"""
Global keyword
"""
score = 0
def update_score(new_score):
    global score
    score = new_score

print(score)
