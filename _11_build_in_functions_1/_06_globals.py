from typing import Any

my_str: str = "Hello World"
my_list: list[Any] = [1, 'A', "ANURAG"]


def my_func():
    ...


print(globals())

for k, v in dict(globals()).items():
    print(f"{k} = {v}")
