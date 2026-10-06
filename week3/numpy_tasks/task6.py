# task6
# Extract the integer part of a random array using 5 different methods
import numpy as np

numbers = np.random.uniform(-10, 10, size=5)

method_1 = numbers.astype(int)
method_2 = np.trunc(numbers)
method_3 = np.fix(numbers)
fractional_parts, method_4 = np.modf(numbers)
method_5 = np.copysign(np.floor(np.abs(numbers)), numbers)

print("Original array:", numbers)
print("Type conversion (astype):", method_1)
print("Truncation (trunc):", method_2)
print("Truncation (fix):", method_3)
print("Split into parts (modf):", method_4)
print("Floor and restore sign:", method_5)