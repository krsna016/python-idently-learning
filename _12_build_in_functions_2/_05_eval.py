result: int = eval("123 + 456")
print(result)

print(eval("print('Hello World')"))

while True:
    user_input: str = input("Enter Math : ")
    print(eval(user_input))
