import sys
from datetime import datetime


def get_response(text: str) -> str:
    response: str = text

    if response in ['hello', 'hi', 'hey']:
        return 'Hey there!'
    elif 'how are you' in response:
        return 'I\'m good. Thanks!'
    elif 'your name' in response:
        return 'My name is: Bot'
    elif 'time' in response:
        return f'The time is : {datetime.now().time():%H:%M}'
    elif response in ['bye', 'see you', 'goodbye']:
        return 'It was nice talking to you.'
    else:
        return f'Sorry I do not understand : {response}'


while True:
    response = input("Enter the prompt : ").lower()
    if response == 'exit':
        sys.exit()
    print(get_response(response))
