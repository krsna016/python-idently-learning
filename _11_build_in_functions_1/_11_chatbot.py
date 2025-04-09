from difflib import get_close_matches


def get_best_match(user_question: str, knowledge: dict[str: str]) -> str | None:
    questions: list[str] = [q for q in knowledge]
    matches: list[str] = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]


def run_chatbot(knowledge: dict) -> None:
    while True:
        user_input: str = input('You : ')
        best_match: str | None = get_best_match(user_input, knowledge)
        response: str | None = knowledge.get(best_match)
        if response:
            print(f"Bot : {response}")
        else:
            print(f'Bot : I do not understand...')


def main() -> None:
    brain: dict[str, str] = {
        "hello": "Hey there!",
        "how are you?": "I am good, thanks!",
        "what is your name?": "I am a chatbot.",
        "bye": "Goodbye! Have a great day!",
        "what do you do?": "I chat with you!",
        "how old are you?": "I am timeless.",
        "where are you from?": "I exist in the cloud.",
        "tell me a joke": "Why did the computer go to the doctor? It caught a virus!",
        "what is Python?": "Python is a programming language.",
        "who created you?": "I was created by a developer.",
        "what is AI?": "AI stands for Artificial Intelligence."
    }
    run_chatbot(knowledge=brain)


if __name__ == "__main__":
    main()
