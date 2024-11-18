user_input: str = input("Enter number : ")
try:
    result: float = 1 / float(user_input)
    print(f"1 / {user_input} = {result}")
except ValueError:
    print(f"You cannot use : {user_input} as a value.")
except ZeroDivisionError:
    print("You cannot divide by Zero.")
else:
    print("Success there were no exceptions encountered.")
finally:
    print("FINALLY: I am always executed!!")
