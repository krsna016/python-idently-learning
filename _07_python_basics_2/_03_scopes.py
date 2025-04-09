"""
In Python, scope refers to the region of a program where a particular variable is accessible. There are four types of scope:

1. **Local Scope**: Variables defined inside a function. They are only accessible within that function.
2. **Enclosing Scope**: Variables in the local scope of enclosing functions. This is relevant for nested functions.
3. **Global Scope**: Variables defined at the top level of a script or module, or declared global using the `global` keyword. They are accessible throughout the module.
4. **Built-in Scope**: Names preassigned in Python. These include functions like `print()`, `len()`, etc.

Python follows the LEGB rule to resolve the scope of a variable:
- **L**ocal
- **E**nclosing
- **G**lobal
- **B**uilt-in

Here is an example to illustrate the different scopes:

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # Prints "local"

    inner()
    print(x)  # Prints "enclosing"

outer()
print(x)  # Prints "global"
"""

"""
Global Scope : Variables defined at the top level of a script or module, 
or declared global using the `global` keyword. They are accessible throughout 
the module. The `global` keyword is used to modify a global variable inside a function.

Built-in Scope : Names preassigned in Python. These include functions like `print()`,
`len()`, etc. The `nonlocal` keyword is used to modify a variable in the enclosing (non-global)
scope.
"""

# var: int = 10
# def outer_func() -> None:
#     global var
#     var = 100
#     print(var)
#     def inner_func() -> None:
#         inner_var: int = 1
#         print(var)
# outer_func()
# print(var)



# def outer_func() -> None:
#     name: str = ''
#     value: int = 0
#     def inner_func() -> None:
#         nonlocal name
#         name = 'Anurag'
#         value = 100
#     inner_func()
#     print(name,value)
# outer_func()
