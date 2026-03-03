# Lab Assignment 2

import numpy as np

print("Enter elements for 5x3 matrix:")
matrix1 = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix1.append(row)

print("Enter elements for 3x2 matrix:")
matrix2 = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix2.append(row)

matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

product = np.dot(matrix1, matrix2)

print("\n5x3 Matrix:")
print(matrix1)

print("\n3x2 Matrix:")
print(matrix2)

print("\nProduct Matrix (5x2):")
print(product)