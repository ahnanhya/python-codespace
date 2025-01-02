import numpy as mat

# Create two matrices
matrix1 = mat.array([[1, 2], [3, 4]])
matrix2 = mat.array([[5, 6], [7, 8]])

# Perform matrix multiplication
result = mat.dot(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nMatrix Multiplication Result:")
print(result)
