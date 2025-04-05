def example_func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    # pos1 and pos2 are positional-only parameters
    # pos_or_kwd can be passed either by position or keyword
    # kwd1 and kwd2 are keyword-only parameters
    pass  # / is used to indicate positional-only parameters

# * is used to indicate keyword-only parameters
# ** is used to collect keyword arguments into a dictionary


# ---------------------------------------------
# 🧠 FUNCTION ARGUMENTS: Use of `/` and `*` in Python
# ---------------------------------------------

# Python allows two powerful symbols in function parameters:
# 1. `/`  → Positional-only parameters
# 2. `*`  → Keyword-only parameters

# ---------------------------------------------
# 🔹 `/` → POSITONAL-ONLY PARAMETERS
# ---------------------------------------------
# All parameters before `/` MUST be passed using POSITION only
# You CANNOT use their names while calling

def func(a, b, /):
    print(a, b)

# ✅ Valid call:
func(1, 2)

# ❌ Invalid call:
# func(a=1, b=2)  # Error: a and b must be positional

# Why use this?
# - Prevent users from relying on parameter names
# - Useful in APIs where parameter names might change in future

# ---------------------------------------------
# 🔸 `*` → KEYWORD-ONLY PARAMETERS
# ---------------------------------------------
# All parameters after `*` MUST be passed using their NAMES (keyword arguments)

def func(*, x, y):
    print(x, y)

# ✅ Valid call:
func(x=10, y=20)

# ❌ Invalid call:
# func(10, 20)  # Error: x and y must be keyword arguments

# Why use this?
# - Forces clarity in function calls
# - Prevents accidental misplacement of values

# ---------------------------------------------
# 💥 COMBINING `/` AND `*`
# ---------------------------------------------
# You can mix both for full control

def introduce(name, age, /, city, *, hobby="Reading"):
    print(f"My name is {name}, I am {age}, from {city}, I love {hobby}.")

# ✅ Valid:
introduce("Aria", 10, "London", hobby="Dancing")

# ❌ Invalid:
# introduce(name="Aria", age=10, city="London")  # name and age must be positional
# introduce("Aria", 10, "London", "Dancing")     # hobby must be keyword

# ---------------------------------------------
# 👨‍💼 PROFESSIONAL EXAMPLE
# ---------------------------------------------
# Design a function for a data science plot

def plot(x, y, /, color="blue", *, grid=True, title="My Plot"):
    print("Plotting with:", x, y, color, grid, title)

# ✅ Proper usage:
plot([1, 2, 3], [4, 5, 6], color="red", grid=False, title="Test Plot")

# ❌ Incorrect usage:
# plot(x=[1, 2], y=[3, 4])  # Error: x and y must be positional
# plot([1, 2], [3, 4], "red", False, "Plot")  # grid and title must be keyword

# ---------------------------------------------
# 🎯 CHALLENGE
# ---------------------------------------------
# Try creating this function with all argument types:

def book_ticket(name, age, /, destination, date="Today", *, seat="Window", meal="Veg"):
    print(f"Name: {name}, Age: {age}, Going to: {destination}, Date: {date}")
    print(f"Seat: {seat}, Meal: {meal}")

# ✅ Example call:
book_ticket("Ravi", 20, "Delhi", seat="Aisle", meal="Non-Veg")

# ❌ Try wrong calls to learn from errors!

# ---------------------------------------------
# 🧠 SUMMARY
# ---------------------------------------------
# `/` → Everything before it is POSITIONAL-ONLY
# `*` → Everything after it is KEYWORD-ONLY
# Use both for writing CLEAN and CLEAR APIs in Python