from typing import override


class Shape:
    def __init__(self, name: str, side: int) -> None:
        self.name = name
        self.side = side

    def describe(self) -> None:
        print(f"{self.name} have {self.side} sides.")

    def shape_method(self) -> None:
        print(f"{self.name} called shape_method()")


class Square(Shape):
    def __init__(self, size: float):
        super().__init__('Square', 4)
        self.size = size

    @override
    def describe(self) -> None:
        print(f"I'm a {self.name} with {self.side} sides.")


class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        super().__init__("Rectangle", 4)
        self.length = length
        self.width = width

    @override
    def describe(self) -> None:
        print(f"{self.name} : {self.length} x {self.width}")


def main() -> None:
    square: Square = Square(20)
    square.describe()
    square.shape_method()

    rectangle: Rectangle = Rectangle(20, 40)
    rectangle.describe()
    rectangle.shape_method()


if __name__ == '__main__':
    main()
