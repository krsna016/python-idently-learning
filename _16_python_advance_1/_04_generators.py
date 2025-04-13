from typing import Generator


# Generator function is a function that returns an iterator that yields values one at a time using the yield keyword.
# We can use a generator function to create an iterator that generates a sequence of values on the fly, rather than storing them in memory.
# This can be useful for working with large datasets or for creating infinite sequences.
# Generator expression is a concise way to create a generator without defining a function.
# We use next() to get the next value from the generator.
# As we retrieve values from the generator, that value is removed from the generator and in the next call to next() the next value is returned.

def five_number() -> Generator:
    for i in range(1, 6):
        yield i


numbers: Generator = five_number()
print(next(numbers))
print(list(numbers))  # As we printed all now the generator is empty


# Since generator is empty now, we can't use it again.
# print(next(numbers))
# print(next(numbers))
# print(list(numbers))


def huge_data() -> Generator:
    for i in range(1, 1000_000_000_000):
        yield i


data: Generator = huge_data()
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))


# print(list(data)) # This will take a lot of time and memory


def generate_vowels() -> Generator:
    vowels: str = "aeiou"
    for vowel in vowels:
        yield vowel


vowels: Generator = generate_vowels()
print(next(vowels))
print(next(vowels))
# When nothing left we get StopIteration error, we can handle it using try and except
