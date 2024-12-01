# In Python, "functions" and "methods" are both definable using the 'def' keyword,
# but they differ in terms of their usage and the context in which they are called.

# A function is a block of code that performs a specific task. It can be defined 
# outside a class and can be called independently.
def my_function():
    print("I am a function!")


# Now to call this function:
my_function()


# A method, on the other hand, is a function that is associated with an object.
# Methods are defined inside a class and can operate on data (attributes) contained 
# within the class.
class MyClass:
    def my_method(self):
        print("I am a method!")


# To call this method, we need to create an instance of the class first:
my_instance = MyClass()
my_instance.my_method()


# Main differences:
# 1. Functions are defined outside of classes, whereas methods are defined within a class.
# 2. Methods have access to the instance (self) which allows them to access and modify 
#    the object’s properties.
# 3. Functions are called by their name directly whereas methods are called on an instance of a class.

# Functions example:
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


print(add(5, 3))
print(subtract(5, 3))


# Methods example:
class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(5, 3))
