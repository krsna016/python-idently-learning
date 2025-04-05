age: int = int(input("Enter your age : "))
if age >= 21:
    print("You may enter the club!")
else:
    print("You are not allowed in...")

weather: str = "Cloudy"
if weather == "Clear":
    print("It's a nice day.")
elif weather == "Cloudy":
    print("The weather could be better...")
elif weather == "Rainy":
    print("What a awful day!")
else:
    print("Unknown weather...")
