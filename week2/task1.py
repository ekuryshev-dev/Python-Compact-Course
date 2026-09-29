import random

# Sample data from the task
tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Uncomment to test with random data
#tuples = [(random.randint(1, 10), random.randint(1, 10)) for i in range(5)]

sorted_tuples = sorted(tuples, key=lambda x: x[-1])

print("Original list:", tuples)
print("Sorted list:", sorted_tuples)