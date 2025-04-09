name: str = input("Enter a name : ")

noun_a: str = input("Enter a noun : ")
verb_a: str = input("Enter a verb : ")
noun_b: str = input("Enter a noun : ")
verb_b: str = input("Enter a verb (past tense) : ")

number_a: str = input("Enter a number : ")
number_b: str = input("Enter another number : ")

story: str = f"""
----------------------------------------------------------------
This is a story about {name}, a strong (and beautiful) {noun_a}
who loved to {verb_a}.

{name} once {verb_b} and won a {noun_b} as a prize.
Isn't that incredible?

Today, {name} is {int(number_a) + int(number_b)} years old and 
has retired from all adventures.

But the story will live on forever...
----------------------------------------------------------------
"""
print(story)
