# task2
# Create a 5x5 array with random values. and find the minimum and maximum values
import numpy as np

matrix = np.random.randint(0, 100, size=(5, 5))
minimum = matrix.min()
maximum = matrix.max()

print("Random 5×5 array:")
print(matrix)
print("Minimum:", minimum)
print("Maximum:", maximum)

# task3
# Normalize a 5x5 random matrix
normalized_matrix = (matrix - minimum) / (maximum - minimum)
print("Normalized matrix:")
print(normalized_matrix)