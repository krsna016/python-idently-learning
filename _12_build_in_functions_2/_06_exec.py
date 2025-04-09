code: str = """
x: int = 10
y: int = 20
print(f'x: {x}, y: {y}')
print("hello world")

for i in range(5):
    print(i)
"""
exec(code)

while True:
    user_input: str = input("Enter the command : ")
    exec(user_input)
