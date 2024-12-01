class MyClass:
    def __init__(self, value):
        # self.value is an instance variable
        # self is a reference to the current instance of the class
        self.this_value = value

    def display(self):
        # self is used to access variables and methods of the current instance
        print(f"The value is {self.this_value}")


if __name__ == "__main__":
    # This block will only be executed if the script is run directly,
    # not if it is imported as a module.

    # Creating an instance of MyClass
    my_instance = MyClass(10)

    # Calling the display method on the instance
    my_instance.display()
