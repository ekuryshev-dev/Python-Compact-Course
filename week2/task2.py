s1 = input("Enter a string: ")

digits = []

for character in s1:
    if character in "0123456789":
        digits.append(int(character))

if digits:
    total = sum(digits)
    average = total / len(digits)
    print("Sum:", total)
    print("Average:", average)
else:
    print("There are no digits in the string")