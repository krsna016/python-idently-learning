class MyClass:
    def __init__(self, attribute1, attribute2):
        """
        The __init__ method is called when an instance of the class is created.
        
        Parameters:
        attribute1: The first attribute for the instance.
        attribute2: The second attribute for the instance.
        """
        # self.attribute1 and self.attribute2 are instance variables.
        # They are initialized with the values provided when an instance is created.
        self.attribute1 = attribute1
        self.attribute2 = attribute2

        # Any additional initialization can be done here
        # For example, you can set default values or call methods to set up the instance

    def display_attributes(self):
        """
        Method to display the attributes of the instance.
        """
        print(f'Attribute 1: {self.attribute1}')
        print(f'Attribute 2: {self.attribute2}')


if __name__ == "__main__":
    # Creating an instance of MyClass
    obj = MyClass('value1', 'value2')

    # Displaying the attributes of the instance
    obj.display_attributes()
