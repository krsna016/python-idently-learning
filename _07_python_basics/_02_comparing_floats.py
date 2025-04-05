from math import isclose

"""
The expression `.1 + .2 == .3` evaluates to `False` due to floating-point precision errors.
Floating-point numbers are represented in a way that can introduce small rounding errors.
As a result, the sum of `.1` and `.2` is not exactly equal to `.3`.
"""
print(.1 + .2 == .3)
print(f".1 + .2 = {.1 + .2}")

# Let us solve the issue :
a: float = 0.999
b: float = 1.000
print(f"{a} == {b} : {a == b}")
print(f"{a} == {b} : {isclose(a, b, abs_tol=.002)}")