class Car:
    def __init__(self, brand: str, wheels: int) -> None:
        """
        Initialize a new Car instance.

        :param brand: The brand of the car.
        :param wheels: The number of wheels the car has.
        """
        self.brand = brand
        self.wheels = wheels

    def turn_on(self) -> None:
        """
        Turn on the car.
        """
        print(f"Turning on...{self.brand}")

    def turn_off(self) -> None:
        """
        Turn off the car.
        """
        print(f"Turning off...{self.brand}")

    def drive(self, km: float) -> None:
        """
        Drive the car for a specified distance.

        :param km: The distance in kilometers to drive the car.
        """
        print(f"Driving {self.brand} for {km} km")

    def describe(self) -> None:
        """
        Describe the car including its brand and number of wheels.
        """
        print(f"{self.brand} is a car with {self.wheels} wheels.")


def main() -> None:
    """
    Main function to demonstrate the usage of the Car class.
    """
    # Create a Car instance with the brand "BMW" and 4 wheels
    bmw: Car = Car("BMW", 4)
    # Print the brand of the car
    print(f"Brand is {bmw.brand}")
    # Print the number of wheels the car has
    print(f"No. of wheels are {bmw.wheels}")
    # Describe the car
    bmw.describe()
    # Turn on the car
    bmw.turn_on()
    # Drive the car for 10.65 kilometers
    bmw.drive(10.65)
    # Turn off the car
    bmw.turn_off()

    print()
    print()

    volvo: Car = Car("Volvo", 3)
    volvo.describe()
    volvo.turn_on()
    volvo.drive(101)
    volvo.turn_off()


if __name__ == '__main__':
    main()
