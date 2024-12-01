class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def drink(self) -> None:
        print(f"{self.name} is drinking.")

    def eat(self) -> None:
        print(f"{self.name} is eating.")


class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def bark(self) -> None:
        print(f"{self.name}: Bark bark !!")

    def routine(self) -> None:
        self.eat()
        self.bark()
        self.drink()


class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def meow(self) -> None:
        print(f"{self.name}: Meow meow !!")


def main() -> None:
    dog: Dog = Dog('Boomerang')
    cat: Cat = Cat("Snowball")

    dog.bark()
    cat.meow()

    dog.eat()
    cat.eat()

    ...


if __name__ == '__main__':
    main()
