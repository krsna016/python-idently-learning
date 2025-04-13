import time
from functools import wraps
from typing import Callable


def get_time(func: Callable) -> Callable:
    """Time how long it takes to run/execute a function."""

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        start_time: float = time.perf_counter()
        func(*args, **kwargs)
        end_time: float = time.perf_counter()

        print(f"Time: {(end_time - start_time):.3f} sec")

    return wrapper


@get_time
def calculate() -> None:
    """calculate() doc-string"""
    for _ in range(20_000_000):
        pass
    print("Done!!")


def main() -> None:
    calculate()
    # Here if we try to print calculate.__name__  and calculate.__doc__ it will return the name and doc-string of the wrapper function
    # because the calculate function is now replaced by the wrapper function, but we can use the wraps decorator to preserve the original function's name and doc-string
    # this is done by using the wraps decorator from the functools module
    # print(calculate.__name__)
    # print(calculate.__doc__)


if __name__ == '__main__':
    main()
