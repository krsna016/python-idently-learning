class Car:
    """
    The Car class defines the blueprint for a car with basic attributes and methods. It includes private,
    protected, and public members to demonstrate encapsulation and name mangling in Python.

    Attributes:
        __YEAR (int): A private attribute representing the manufacture year of the car. Not accessible from subclasses.
        _YEAR_OTHER (int): A protected attribute that can be accessed from subclasses.
    """
    __YEAR: int = 2000
    _YEAR_OTHER: int = 2001

    def __init__(self, brand: str, fuel_type: str) -> None:
        """
        Initializes a Car object with a brand and fuel type.

        Args:
            brand (str): The brand of the car.
            fuel_type (str): The type of fuel used by the car.
        """
        self.__brand = brand
        self.__fuel_type = fuel_type
        self.__var: str = 'red'

    def drive(self) -> None:
        """
        Simulates driving the car by printing its brand.
        """
        print(f"Driving {self.__brand}.")

    def __get_description(self) -> None:
        """
        Prints the description of the car, including its private brand and fuel type attributes. This method
        is private and cannot be accessed directly outside the class.
        """
        print(f"{self.__brand} is {self.__fuel_type} car.")

    def display_colour(self) -> None:
        """
        Displays the color of the car by accessing its private color variable.
        """
        print(f"{self.__brand} is '{self.__var.capitalize()}'")


class Toyota(Car):
    """
    The Toyota class inherits from the Car class and represents a specific car brand. It demonstrates access
    to protected members from the parent class.
    """

    def __init__(self, fuel_type: str):
        """
        Initializes a Toyota object with a specified fuel type. Inherits the brand name 'Toyota'.

        Args:
            fuel_type (str): The type of fuel used by the Toyota car.
        """
        super().__init__('Toyota', fuel_type)
        self.var = 100

    # Name mangling prevents direct access to __YEAR in Car
    # def get_year(self) -> int:
    #     return self.__YEAR

    def get_year(self) -> int:
        """
        Returns the year of manufacture by accessing the protected _YEAR_OTHER attribute from the parent class.

        Returns:
            int: The year related to _YEAR_OTHER.
        """
        return self._YEAR_OTHER


def main() -> None:
    """
    The main function serves as the entry point to the program, creating a Toyota car object,
    displaying its attributes and calling methods to demonstrate encapsulation.
    """
    # car: Car = Car("Toyota", 'Electric')
    # car.drive()
    # print(car._Car__brand)
    # car._Car__get_description()

    toyota: Toyota = Toyota('Electric')
    print(toyota.var)
    toyota.display_colour()
    print(toyota.get_year())
    ...


if __name__ == '__main__':
    main()
