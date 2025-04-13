import time
from functools import cached_property


class Dataset:
    def __init__(self, data: list[float]):
        self._data = data

    def show_data(self) -> None:
        print(self._data)

    @cached_property
    def sum_data(self) -> float:
        print("Calculating sum...")
        time.sleep(3)
        return sum(self._data)

    @cached_property
    def mean_data(self) -> float:
        print("Calculating mean...")
        time.sleep(3)
        return sum(self._data) / len(self._data)


def main() -> None:
    ds: Dataset = Dataset([1.4, 5.6, 8.4, 9.6])
    ds.show_data()
    while True:
        user_input: str = input("You: ")
        if user_input == 'clear sum':
            del ds.sum_data  # This will clear the cache, but we need to call it once before deleting it else it will raise an error
            print("sum_data cleared")
        elif user_input == 'clear mean':
            del ds.mean_data  # This will clear the cache, but we need to call it once before deleting it else it will raise an error
            print("mean_data cleared")
        elif user_input == 'sum':
            print(ds.sum_data)
        elif user_input == 'mean':
            print(ds.mean_data)
        else:
            print("Invalid command")


if __name__ == '__main__':
    main()
