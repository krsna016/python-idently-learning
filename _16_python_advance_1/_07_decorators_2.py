from functools import wraps
from typing import Callable, Any


def repeat(number: int) -> Callable:
    """
    Decorator to repeat the function call x amount of times.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            value: Any = None
            for _ in range(number):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


@repeat(number=3)
def greet(name: str) -> int:
    """Function used to greet people"""
    print(f"Hello, {name}!!")
    # print(greet.__name__)
    # print(greet.__doc__)
    return 0


def main() -> None:
    greet(input("Enter the name : "))


if __name__ == '__main__':
    main()
