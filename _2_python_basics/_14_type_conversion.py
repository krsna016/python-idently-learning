txt_value: str = "100"
int_value: int = 50

# print(txt_value + int_value) # Give error
print(int(txt_value) + int_value)

print(txt_value + str(int_value))

# In Python, the following data types can be concatenated:
#
# 1. Strings: You can concatenate strings using the `+` operator.
#    "Hello, " + "world!"  # "Hello, world!"
#
# 2. Lists: You can concatenate lists using the `+` operator.
#    [1, 2, 3] + [4, 5, 6]  # [1, 2, 3, 4, 5, 6]
#
# 3. Tuples: You can concatenate tuples using the `+` operator.
#    (1, 2, 3) + (4, 5, 6)  # (1, 2, 3, 4, 5, 6)
#
# The following data types cannot be concatenated directly:
#
# 1. String and Integer: You cannot concatenate a string and an integer directly.
#    "Number: " + 5  # TypeError: can only concatenate str (not "int") to str
#
# 2. String and Float: You cannot concatenate a string and a float directly.
#    "Value: " + 3.14  # TypeError: can only concatenate str (not "float") to str
#
# 3. List and String: You cannot concatenate a list and a string directly.
#    [1, 2, 3] + "456"  # TypeError: can only concatenate list (not "str") to list
#
# Floats and Ints can be added and result is float.
#
# To concatenate incompatible types, you need to convert them to compatible types first, usually by converting non-string types to strings using the `str()` function.

print(10 + 5.6)
print(10 + 290.0)
