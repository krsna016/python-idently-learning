"""Talking about : F-String"""

# F-String: A concise and readable way to embed expressions inside string literals in Python.
var: int = 10


def add(a: int, b: int) -> int:
    return a + b


print(f"{var=}")
print(f"{add(5,10) = }")

big_num: float = 123456789
print(f'{big_num:,}')
print(f'{big_num:_}')

big_num: float = 123_45_6789  # Possible

fraction: float = 1234.5678
print(f'{fraction:.2f}')
print(f'{fraction:,.2f}')

percent: float = 0.5555
print(f'{percent:.2%}')
print(f'{percent:.0%}')

var: str = "BOB"
print(f'{var:10}: Hello')
print(f'{var:>10}: Hello')
print(f'{var:^10}: Hello')
print(f'{var:<10}: Hello')

print(f'{var:.^10}: Hello')

numbers: list[int] = [1, 100, 1_000, 10_000]
for number in numbers:
    print(f'{number:_>5}')

"""Talking About R-String"""
# R-String: A raw string in Python where backslashes are treated as literal characters.
# Example: Useful for file paths or regular expressions.path: str = '\\Users\\anurag\\Documents'
path: str = r'\Users\anurag\Documents'
user: str = 'anurag'
path: str = fr'\Users\{user}\Documents'
