import string


def is_letters_only(text: str) -> None:
    alphabets: str = string.ascii_letters + " "
    for char in text:
        if char not in alphabets:
            raise ValueError("Text can only contain letters of alphabets.")
    print(f"Good Job! {text} is letters only.")


def main() -> None:
    while True:
        is_letters_only(input("Enter text : "))
