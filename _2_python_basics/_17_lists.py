from typing import Any

my_list: list[Any] = [1, 2, 3, 4, "Hello"]
print(my_list)

another_list: list[int] = [6, 7, 8]
combined_list: list[Any] = my_list + another_list
print(combined_list)

print(my_list[0:2])  # First element
print(my_list[-1])  # Last element

print(my_list)

for item in my_list:
    print(item)

list_1: list[Any] = []
list_1.append("Anurag")
list_1.append([1, 2, 3])
list_1.remove("Anurag")

print(list_1)

# Example of list operations
example_list: list[int] = [1, 2, 3, 4, 5]

# Append an element
example_list.append(6)
print("After append:", example_list)

# Insert an element at a specific position
example_list.insert(2, 10)
print("After insert:", example_list)

# Remove an element
example_list.remove(10)
print("After remove:", example_list)

# Pop an element
popped_element = example_list.pop()
print("After pop:", example_list)
print("Popped element:", popped_element)

# Reverse the list
example_list.reverse()
print("After reverse:", example_list)

# Sort the list
example_list.sort()
print("After sort:", example_list)

# Clear the list
example_list.clear()
print(example_list)
