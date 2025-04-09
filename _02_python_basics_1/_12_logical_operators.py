a: int = 1
b: int = 5
c: int = 10
d: int = 10

print(a < b and b < c)  # True
print(a > b or b < c)  # True
print(not (a > b))  # True

print(a < b and b < c)  # True
print(a > b or b < c)  # True
print(not (a > b))  # True

# Truth table for logical operators
# A     B     A and B     A or B     not A
# True  True  True        True       False
# True  False False       True       False
# False True  False       True       True
# False False False       False      True

print(not 0)  # True because 0 is considered False, and not False is True and every other number is considered as True
