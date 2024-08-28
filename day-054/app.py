import numpy as np


a = np.array([1, 2, 3], dtype=np.int16)
print(a)

b = np.array([[8.0, 7.0, 6.0], [5.0, 4.0, 3.0]])
print(b)


# Get Dimensions
print(a.ndim)
print(b.ndim)

# Get shape
print(a.shape)
print(b.shape)

# Get type 
print(a.dtype)
print(b.dtype)

# Get size
print(a.itemsize)
print(b.itemsize)

# Get Total Size
print(a.size)
print(b.size)

a = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18]], dtype=np.int16)
print(a)


# Get specific element [r, c] 

print(a[1, 6])
# Get a specific row 
print(a[0, :])

# Get a specific column
print( a[:, 4] )

# Get a little more fancy [start-index:end-index:step-index]
print(a[0, 1:6:2])

# Set value
a[1, 6] = 50
print(a)

# Set value column
a[:, 2] = [20]
print(a)
a[:, 2] = [1, 1]
print(a)

## Initializing arrays

# All 0s matrix
temp = np.zeros((3, 3), dtype=np.int16)
print(temp)

# All 1s matrix
temp = np.ones((3, 3), dtype=np.int16)
print(temp)

# Any other number
temp = np.full((4, 4), 99, dtype=np.int32)
print(temp)

# Any other number full_like
temp = np.full_like(a, 55)
print(temp)

# Random numbers decimal
temp = np.random.random((3, 5))
print(temp)

# Ramdom number int
temp = np.random.randint(1, 10, size=(3, 3))
print(temp)

# The indentity matrix
temp = np.identity(5)
print(temp)

# Repeat an array
base = np.array([[1, 2, 3]])
temp = np.repeat(base, 3)
print(temp)
temp = np.repeat(base, 3, axis=0)
print(temp)

# Update matrix
#[[1. 1. 1. 1. 1.]
# [1. 0. 0. 0. 1.]
# [1. 0. 9. 0. 1.]
# [1. 0. 0. 0. 1.]
# [1. 1. 1. 1. 1.]]

result = np.ones(( 5, 5 ))
print(result)
inner = np.zeros(( 3, 3 ))
print(inner)
inner[1, 1] = 9
print(inner)
result[1:4,1:4] = inner;
print(result)

## Mathematics
print("====================")
a = np.array([1, 2, 3, 4])
print("Original ...")
print(a)
print("Array + 2")
print(a + 2)
print("Array * 2")
print(a * 2)
a += 2
print(a)

# Basic Operations
print(np.cos(a))

## Linear Algebra
a = np.full((2, 3), 2)
b = np.full((3, 2), 3)
print(a)
print(b)
# Algebra Multiplication
print( np.matmul(a, b) )
# Find the determinat
a = np.array([[2, 2, 2], [4, 4, 4], [7, 8, 9]])
print(np.linalg.det(a))

## Statics
a = np.array([[12, 4, 5, 9, 7], [2, 14, 7, 5, 12]])
#min
print(np.min(a))
#max
print(np.max(a))

## Reorganization Array
# reshape
a = np.ones((4,2))
print(a)
print(np.reshape(a, (2, 4)))

## Stack
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Vertical stacking  
result = np.vstack([a, b, a])
print(result)

# Horizontal stacking
result = np.hstack([a, b])
print(result)

#Load dato from file

result = np.genfromtxt('../data/numbers.csv', delimiter=',')
result.astype(np.int32)
print(result)

a = np.any(result > 10) 
print(a)
a = np.any(result > 10, axis=0) 
print(a)
a = np.any(result > 10, axis=1) 
print(a)

"""
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
26 27 28 29 30
"""
a = np.array([
    [1, 2, 3, 4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30]
    ])

result = a[2:4, 0:2] 
print(result)

result = a[[0,1,2,3], [1,2,3,4]] 
print(result)

result = a[[0,4,5], 3:5] 
print(result)
