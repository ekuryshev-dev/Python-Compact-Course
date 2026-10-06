# task4
# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
import numpy as np

matrix_a = np.random.randint(0, 10, size=(5, 3))
matrix_b = np.random.randint(0, 10, size=(3, 2))

result_matrix = matrix_a @ matrix_b

print("Matrix A (5×3):")
print(matrix_a)
print("Matrix B (3×2):")
print(matrix_b)
print("Result matrix:")
print(result_matrix)