no_value: None = None
print(no_value)
print(type(no_value))

users: dict = {1: "Mario", "Hello": "World"}
# Instead of - print(users[4]), We can use get() to avoid key error
print(users.get(4))

possible_user: str | None = users.get(10)
print(possible_user)
