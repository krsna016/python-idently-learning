for i in range(4):
    """
    This for loop iterates from 0 to 3 and prints the current iteration number.
    After the loop completes, it prints "Successful...".
    """
    print(f"Iteration : {i}")
else:
    print("Successful...")

i: int = 10
while True:
    print(i)
    if i == 5:
        break
    i -= 1
else:
    print("Successful...")  # This code now is unreachable
