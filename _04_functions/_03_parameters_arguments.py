def greet_me(name: str) -> None:
    print("Hello,", name)


greet_me("Anurag")


def add_two(a: int, b: int) -> int:
    return a + b


print(add_two(1, 2))


def greet_us(lang: str, default: str = "Hello") -> None:
    if lang == "Namaste":
        print(lang)
    else:
        print(default)


greet_us("Ciao")
