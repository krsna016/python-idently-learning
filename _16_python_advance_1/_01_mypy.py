var: str = 10  # Here due to type hinting, python will throw an error

items: list[str] = ['Cup', 'Apple', True, [1, 2, 3]]  # But here python will not throw an error


# Hence we use mypy to check the type hinting, this is a static type checker which can be used to check the type hinting in the code
# To install mypy, use the command: pip install mypy or for conda environment: conda install mypy
# To check the type hinting in the code, use the command: mypy <filename>.py in terminal

def func(var: int = None):
    ...
