# task1
# Create a vector with values ranging from 10 to 49. Reverse a vector (first element becomes last)
import numpy as np

vector = np.arange(10, 50)
reversed_vector = vector[::-1]

print("Original: ", vector)
print("Reversed: ", reversed_vector)