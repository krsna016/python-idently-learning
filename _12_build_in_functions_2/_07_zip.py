number: list[int] = [1, 2, 3, 4]
letters: list[str] = ['A', 'B', 'C', 'D']
symbol: list[str] = ['!', '^', '*']

zipped: zip = zip(number, letters)
for n, l in zipped:
    print(n, l, sep=" -> ")

zipped: zip = zip(number, symbol)
for n, l in zipped:
    print(n, l, sep=" -> ")

# zipped: zip = zip(number, symbol, strict=True)
# for n, l in zipped:
#     print(n, l, sep=" -> ")

zipped: zip = zip(number, symbol, letters)
print(list(zipped))
