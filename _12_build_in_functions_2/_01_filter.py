number: list[int] = list(range(1, 21))


def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0


evens: filter = filter(is_even, number)
list(evens)

# Also:

more_evens: list[int] = list(filter(lambda x: x % 2 == 0, list(range(1, 101))))
print(more_evens)

length_up_to_four: list[str] = list(filter(lambda x: len(x) <= 4, ['Anurag', 'Ravi', 'Riya', 'Abhijit']))
print(length_up_to_four)

# Also:

print([name for name in ['Anurag', 'Ravi', 'Riya', 'Abhijit'] if len(name) <= 4])
