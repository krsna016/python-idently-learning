# elements: list[str] = ['A', 'B', 'C']
# i: int = 0
# for i, element in enumerate(elements, 2):
#     print(f"{i} : {element}")


elements: list[str] = ['A', 'B', 'C']
enumeration: enumerate = enumerate(elements, start=4)
print(list(enumeration))
for i, element in enumeration:
    print(f"{i} : {element}")
