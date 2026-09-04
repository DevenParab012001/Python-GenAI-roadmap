import numpy as np

# NumPy Roadmap Practice
# Scope: array creation, indexing/slicing, reshaping,
# vectorized computations, mathematical functions, and broadcasting.

# 1. Creating arrays
a = np.array([10, 20, 30, 40, 50])
print("array:", a)

b = np.arange(1, 11)
print("arange:", b)

c = np.linspace(0, 1, 5)
print("linspace:", c)

# 2. Indexing and slicing
print("first element:", a[0])
print("last element:", a[-1])
print("slice:", a[1:4])

# 3. Reshaping
numbers = np.arange(1, 7)
matrix = numbers.reshape(2, 3)
print("reshaped matrix:")
print(matrix)

# 4. Vectorized computations
marks = np.array([70, 80, 90, 85])
print("marks + 5:", marks + 5)
print("marks * 2:", marks * 2)

# 5. Mathematical functions
values = np.array([10, 20, 30, 40, 50])
print("sum:", np.sum(values))
print("mean:", np.mean(values))
print("std:", np.std(values))

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("dot product:", np.dot(x, y))

# 6. Broadcasting
marks = np.array([70, 80, 90])
marks = marks + 5
print("broadcasting:", marks)

# 7. Multi-dimensional data
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D matrix:")
print(matrix)
print("matrix + 10:")
print(matrix + 10)
