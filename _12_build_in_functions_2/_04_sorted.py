numbers: list[int] = [1, 10, 5, 3]
sorted_numbers: list[int] = sorted(numbers)
print(sorted_numbers)

people: list[str] = ['Mario', 'James', 'Anna', 'anurag', 'Tom']
sorted_names: list[str] = sorted(people, reverse=True)
print(sorted_names)

people: list[str] = ['Mario', 'James', 'Anna', 'anurag', 'Tom']
sorted_names: list[str] = sorted(people, key=lambda x: len(x))
print(sorted_names)


class Animal:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f'{self.name} = {self.weight}kg'


animal_1: Animal = Animal('Cow', 100)
animal_2: Animal = Animal('Dog', 20)
animal_3: Animal = Animal('Elephant', 500)

sorted_animals: list[Animal] = sorted([animal_1, animal_2, animal_3], key=lambda x: x.weight)
print(sorted_animals)
