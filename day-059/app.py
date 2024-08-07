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


