numbers: list[int] = [1, 2, 3, 4, 5]
print(numbers[2:4])

text: str = 'Hello World'
print(text[0:3])

my_slice: slice = slice(0, 3)
print(text[my_slice])

rev_slice = slice(None, None, -1)
print(text[rev_slice])

print(text[-5:])
print(text[::2])
