class Person:
    """
    A class to represent a person.

    Attributes
    ----------
    name : str
        The name of the person.
    age : int
        The age of the person.
    """

    species = "Homo sapiens"  # Adding a class attribute

    def __init__(self, name: str, age: int):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
        name : str
            The name of the person.
        age : int
            The age of the person.
        """
        # Assigning the value of the 'name' parameter to the instance attribute 'name'.
        self.name = name
        # Assigning the value of the 'age' parameter to the instance attribute 'age'.
        self.age = age

    def greet(self):
        """
        Function to greet the person.

        Returns
        -------
        str
            A greeting string.
        """
        # Accessing the instance attributes 'name' and 'age'
        return f"Hello, my name is {self.name} and I am {self.age} years old."


if __name__ == "__main__":
    # Create an instance of the Person class
    person = Person("Alice", 30)

    # Access the attributes and call the method
    print(person.name)  # Outputs: Alice
    print(person.age)  # Outputs: 30
    print(person.greet())  # Outputs: Hello, my name is Alice, and I am 30 years old.
