from typing import Self


class Car:
    def __init__(self, brand: str, car_id: int, colour: str) -> None:
        self.brand = brand
        self.car_id = car_id
        self.colour = colour

    def __eq__(self, other: Self) -> bool:
        return self.__dict__ == other.__dict__


def main() -> None:
    car1 = Car("BMW", 1, "Red")
    car2 = Car("BMW", 1, "Red")
    print(car1.__dict__)
    print(car2.__dict__)
    print(car1 == car2)
    ...


if __name__ == '__main__':
    main()
