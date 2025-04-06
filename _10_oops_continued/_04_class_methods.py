from typing import Self

class Car:
    LIMITER: int = 200

    def __init__(self, brand: str, max_speed: int) -> None:
        self.brand = brand
        self.max_speed = max_speed

    @classmethod
    def change_limit(cls, new_limit: int) -> None:
        cls.LIMITER = new_limit

    @classmethod
    def autogenerate_max_speed(cls, brand: str) -> Self:
        lowered: str = brand.lower()
        max_speed: int = 200

        if lowered == 'toyota':
            max_speed = 270
        elif lowered == 'BMW':
            max_speed = 290
        elif lowered == 'volvo':
            max_speed = 300

        return cls(brand, max_speed)

    def display_info(self) -> None:
        print(f"{self.brand} (Max speed: {self.max_speed}, LIMITER: {self.LIMITER})")


def main() -> None:
    # car: Car = Car("Toyota", 120)
    # car.display_info()
    # car.change_limit(150)
    # car.display_info()

    volvo: Car = Car.autogenerate_max_speed('Volvo')
    volvo.display_info()
    ...


if __name__ == '__main__':
    main()
