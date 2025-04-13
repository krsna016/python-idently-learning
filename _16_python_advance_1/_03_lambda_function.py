from typing import Callable

# Lambda function is a small anonymous function that can take any number of arguments
p = lambda x: print(x)
p(10)
p("Hello")

add_two = lambda a, b: a + b
add_two(9, 3)


def use_all(f: Callable, values: list[int]) -> None:
    for value in values:
        f(value)


use_all(lambda x: print(f'{x * 'X'}'), [2, 3, 6])

names: list[str] = ['Bob', 'James', 'Samantha', 'Joe']
print(sorted(names, key=lambda x: len(x)))  # Short based on len
