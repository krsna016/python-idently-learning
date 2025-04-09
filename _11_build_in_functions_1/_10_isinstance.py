"""
isinstance(object, classinfo):
object → The variable or object you are checking.
classinfo → The type (like int, str, list, etc.) or even a tuple of types
"""

number: int = 10
pi: float = 3.14
text: str = 'banana'
my_list: list[int] = [1, 2, 3]

print(isinstance(number, int))
print(isinstance(text, str))
print(isinstance(my_list, list))
print(isinstance(text, float))
print(isinstance(text, float | str))


class Animal:
    pass


class Cat(Animal):
    pass


print(isinstance(Cat(), Animal))
