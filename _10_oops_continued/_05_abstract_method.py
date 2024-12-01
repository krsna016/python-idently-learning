from abc import ABC, abstractmethod


class Appliance(ABC):
    """
    An abstract base class for all appliances.

    Attributes:
        brand (str): The brand of the appliance.
        version_number (int): The version number of the appliance.
        is_turned_on (bool): The current state of the appliance, where True represents that it is turned on.
    """

    def __init__(self, brand: str, version_number: int) -> None:
        """
        Initializes the appliance with a brand and version number.

        Args:
            brand (str): The brand of the appliance.
            version_number (int): The version number of the appliance.
        """
        self.brand = brand
        self.version_number = version_number
        self.is_turned_on: bool = False

    @abstractmethod
    def turned_on(self) -> None:
        """Turns on the appliance."""
        ...

    @abstractmethod
    def turned_off(self) -> None:
        """Turns off the appliance."""
        ...


class Lamp(Appliance, ABC):
    """
    A concrete class representing a lamp, which is a type of appliance.

    Inherits from Appliance class and implements its abstract methods.
    """

    def __init__(self, brand: str, version_number: int):
        """
        Initializes the Lamp with a brand and version number.

        Args:
            brand (str): The brand of the lamp.
            version_number (int): The version number of the lamp.
        """
        super().__init__(brand, version_number)

    def turned_on(self) -> None:
        """Turns on the lamp if it is not already on."""
        if self.is_turned_on:
            print(f"{self.brand} is already turned on...")
        else:
            self.is_turned_on = True
            print(f"{self.brand} is now turned on.")

    def turned_off(self) -> None:
        """Turns off the lamp if it is not already off."""
        if self.is_turned_on:
            self.is_turned_on = False
            print(f"{self.brand} is now turned off.")
        else:
            print(f"{self.brand} is already turned off...")


def main() -> None:
    lamp: Lamp = Lamp("Philips", 123)

    lamp.turned_on()
    lamp.turned_on()
    lamp.turned_off()
    lamp.turned_off()

    ...


if __name__ == '__main__':
    main()
