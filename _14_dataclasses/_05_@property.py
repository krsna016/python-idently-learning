from dataclasses import dataclass


@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float

    # The @property decorator is used to define a method as a property.
    # This allows us to calculate the total price dynamically whenever it is accessed,
    # instead of relying on a fixed value set during initialization (as with __post_init__).
    @property
    def total_price(self) -> float:
        return (self.grams / 100) * self.price_per_kg

    def describe(self) -> None:
        print(f"""{self.grams} grams of {self.name} costs {self.total_price} dollars.""")


def main() -> None:
    apple: Fruit = Fruit("Apple", 1500, 5)

    print(apple)
    apple.describe()

    # Changing the price_per_kg dynamically updates the total_price
    # because @property recalculates it on access, unlike __post_init__ which runs only once.
    apple.price_per_kg = 10
    print(apple)
    apple.describe()


if __name__ == '__main__':
    main()
