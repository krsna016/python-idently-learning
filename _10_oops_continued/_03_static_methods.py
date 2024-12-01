class Calculator:
    def __init__(self, version: float) -> None:
        self.version = version

    @staticmethod
    def add(*numbers: float) -> float:
        return sum(numbers)

    def get_version(self) -> None:
        print(f"Calculator - {self.version}")


def main() -> None:
    calc: Calculator = Calculator(10.23)
    print(calc.add(1, 2, 3, 4, 5, 6, 7, 8))
    # Also
    print(Calculator.add(1, 2, 3, 4, 5, 6, 7, 8))
    calc.get_version()
    ...


if __name__ == '__main__':
    main()
