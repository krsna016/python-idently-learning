import random

print("!! Welcome to our R-P-S Game !!")

moves: dict = {'rock': '🪨', 'paper': '📄', 'scissor': '✂️'}
valid_moves: list[str] = list(moves.keys())

game_status: bool = True

ai_score: int = 0
user_score: int = 0

while game_status:
    print("- - - - - - - - - - - - - - - - -")
    # User Decides:
    user_moves: str = input("Choose - Rock, Paper or Scissor? : ").lower()

    if user_moves == 'exit':
        print("Thanks for playing...\n- - - - - - - - - - - - - - - - -")
        break

    if user_moves not in valid_moves:
        print("Invalid move... Try Again !!")
        continue
    # AI Decides:
    ai_moves: str = random.choice(valid_moves)
    print("- - - - - - - - - - - - - - - - -")

    # Result:
    print(f"YOU : {moves[user_moves]}\nAI : {moves[ai_moves]}")
    if user_moves == ai_moves:
        print("Game Ties...")
    elif user_moves == 'rock' and ai_moves == 'scissor':
        print("You Wins...")
        user_score += 1
    elif user_moves == 'scissor' and ai_moves == 'paper':
        print("You Wins...")
        user_score += 1
    elif user_moves == 'paper' and ai_moves == 'rock':
        print("You Wins...")
        user_score += 1
    else:
        print("AI Wins...")
        ai_score += 1

if user_score == ai_score:
    print("Match Tied !!!")
if user_score > ai_score:
    print(f"You wins with +{user_score - ai_score} scores with AI...")
else:
    print(f"AI wins with +{ai_score - user_score} scores with USER...")
