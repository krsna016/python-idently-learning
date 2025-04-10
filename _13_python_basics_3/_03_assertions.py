"""
An assertion is a statement in programming that you use to test if something is true at a particular point in your code.

📌 It’s like asking your program:
“Hey! 🤨 Are you sure this thing is the way I expect it to be?”

If yes ✅, nothing happens.
If no ❌, your program will stop immediately and usually show an error.
"""


def start_program(db: dict[int, str]) -> None:
    assert db, 'Database is Empty !!'

    print(f'Loaded : {db}')
    print('Program started Successfully')


var: str = 'Anurag'
assert len(var) < 5, 'Length of var is more than 5'
