print("Hello World")
print(1, 2, 3 + 3j, "A", "Hello")
print(1, 2, 3 + 3j, "A", "Hello", sep="-")
print(1, 2, 3 + 3j, "A", "Hello", sep="-", end=".\n")

people: list[str] = ['Mario', 'James', 'Hannah']
print(*people, sep=", ", end=".")
