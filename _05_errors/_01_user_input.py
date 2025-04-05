import sys

total: int = 0
while True:
    user_input: str = input("Enter a number : ")
    if user_input == '0':
        print(f"Total : {total}")
        sys.exit()
    else:
        total += int(user_input)
