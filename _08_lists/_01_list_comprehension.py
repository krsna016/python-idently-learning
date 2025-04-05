numbers: list[int] = [1, 2, 3, 4]
numbers: list[int] = [i * 2 for i in numbers]
print(numbers)

name: list[str] = ["anurag", "radha", "krishna"]
a_names: list[str] = [i for i in name if i[0] == 'a']
print(a_names)

evens: list[int] = [i for i in range(101) if i % 2 == 0]
print(evens)
