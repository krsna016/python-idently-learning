while True:
    user_input: str = input("Enter a number : ")
    try:
        number: float = float(user_input)
        print(f"You entered : {number}")
    except ValueError:
        print(f"The value you entered : {user_input} is invalid.")
    except Exception as e:
        print("Program encountered a new exception...")
        print(f"Error - {e}")
        print(f"Type : {type(e)}")
