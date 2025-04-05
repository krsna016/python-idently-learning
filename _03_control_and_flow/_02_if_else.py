number: int = 0
if number > 0:
    result: str = "Above 0"
else:
    result: str = "Below 0 or 0"
print(result)
# Also,
result: str = 'Above 0' if number > 0 else 'Below 0 or 0'
print(result)

condition: bool = True
result: str = "True" if condition else "False"
print(result)
