"""MULTIPLE ASSIGNMENT"""

a, b, c = 5, 10, 15
print(a, b)

x, y = "XY"
print(x, y)

a, *b = "Hello World !!"
print(a, b)
print(*b)

a, *b, c = 'Hello World'
print(a, c)
print(b)

"""
🛑 NOTE: * can only appear once during unpacking!
# --------------------------------------------
# 🔠 SYMBOL MEANINGS OF UNDERSCORE IN PYTHON
# --------------------------------------------

_         : “Throwaway” or “I don’t care” variable, commonly used to indicate unused values
*_, x     : Used to grab the last value while ignoring the rest
x, *_     : Grab the first value, ignore the rest
_, x, _   : Sometimes used to extract a middle value while ignoring the rest

✅ These are super useful in unpacking sequences like lists, tuples, or strings!
"""

*_, last = "Hi Anurag !!"
print(_)
print(last)

"""UNPACKING"""


def add(a: int, b: int) -> None:
    print(f'{a+b =}')


numbers: dict[str, int] = {'a': 5, 'b': 10}
add(**numbers)

numbers: list[int] = [1, 2, 3, 4, 5]
params: dict[str, str] = {'sep': '-', 'end': '.'}
print(*numbers, **params)
