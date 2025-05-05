from dataclasses import dataclass, field, InitVar


@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float
    # InitVar is used for variables that are passed to the constructor (__init__)
    # but are not stored as instance attributes. They are only used during initialization.
    is_rare: InitVar[bool | None] = None
    total_price: float = field(init=False)

    def __post_init__(self, is_rare: bool | None) -> None:
        if is_rare:
            self.price_per_kg *= 2

        self.total_price: float = (self.grams / 1000) * self.price_per_kg

    def describe(self) -> None:
        print(f"""{self.grams} grams of {self.name} costs {self.total_price} dollars.""")


def main() -> None:
    apple: Fruit = Fruit("Apple", 1500, 5)
    orange: Fruit = Fruit("Orange", 2500, 8)
    passion: Fruit = Fruit("Passion", 100, 50, is_rare=True)

    print(apple)
    print(orange)
    print(passion)

    print(passion.is_rare)

    apple.describe()
    orange.describe()
    passion.describe()


if __name__ == '__main__':
    main()
