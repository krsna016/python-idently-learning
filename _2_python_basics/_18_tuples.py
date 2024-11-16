# Creating a tuple

# We need to annotate type like this in tuple
my_tuple: tuple[int, int, int, str, float] = (1, 2, 3, 'Hello', 4.5)  # We can also make it without parenthesis

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: Hello

# Tuples can be nested
nested_tuple = (1, (2, 3), 4)
print(nested_tuple[1])  # Output: (2, 3)

# Tuples are immutable
# The following line will raise an error
# my_tuple[0] = 10

coordinates = ()
