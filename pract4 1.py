# Lab Assignment 1 (a)

import numpy as np

identity_matrix = np.eye(4)

print("4x4 Identity Matrix:")
print(identity_matrix)

print("----------------x---------------\n")

# Lab Assignment 1 (b)

import numpy as np

# Generate two 3x3 matrices with random integers (1 to 9)
matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Addition
addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)

# Multiplication
multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(multiplication)