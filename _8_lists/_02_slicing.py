# Example of slicing

# Original list
numbers: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing the list
first_five: list[int] = numbers[:5]  # First five elements
last_five: list[int] = numbers[-5:]  # Last five elements
middle: list[int] = numbers[2:7:2]  # Elements from index 2 to 6

print("First five:", first_five)
print("Last five:", last_five)
print("Middle elements:", middle)
