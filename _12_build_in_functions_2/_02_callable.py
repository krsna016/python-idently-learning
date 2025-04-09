fruit: str = "Apple"
number: int = 10


def func() -> None:
    print('func() called')


print(f'is fruit Callable(): {callable(fruit)}')
print(f'is number Callable(): {callable(number)}')
print(f'is func() Callable(): {callable(func)}')

if callable(func):
    func()
else:
    print('func()/Object is not callable')
