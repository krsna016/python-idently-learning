from datetime import datetime
from random import choice


class ChatBot:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_description(self) -> str:
        return f"{self.name} is a bot whose age is {self.age}."

    def get_response(self, text: str) -> str:
        lowered: str = text.lower()
        if 'hello' in lowered:
            return f'Hey there!!'
        elif 'bye' in lowered:
            return f'See you'
        elif 'how are you' in lowered:
            return 'I am just a bot, but thanks for asking!'
        elif 'time' in lowered:
            return f'The current time is {datetime.now():%H:%M:%S}.'
        elif 'date' in lowered:
            return f'Today\'s date is {datetime.now():%Y-%m-%d}.'
        elif 'age' in lowered:
            return f'I am {self.age} years old.'
        elif 'name' in lowered:
            return f'My name is {self.name}.'
        elif 'greet' in lowered:
            return 'Hello! Nice to meet you!'
        else:
            responses = [
                'I am not sure how to respond to that.',
                'Can you please clarify?',
                'Sorry, I didn\'t get that.',
                'Hmm, that\'s interesting.',
                'Could you please say that again?'
            ]
            return choice(responses)
