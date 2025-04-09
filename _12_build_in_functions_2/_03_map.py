numbers: list[int] = [1, 2, 3, 4, 5]
letters: list[str] = ['a', 'b', 'c']

# def double(number: int) -> int:
#     return number * 2
#
# doubled: map = map(double, numbers)
# print(list(doubled))

# Also:
doubled: map = map(lambda x: x * 2, numbers)
print(list(doubled))

# Also:
doubled: list[int] = [n * 2 for n in numbers]
print(doubled)


# Now:
def combine_elements(num: int, letter: str) -> tuple[int, str]:
    return num, letter


combined: map = map(combine_elements, numbers, letters)
print(list(combined))
