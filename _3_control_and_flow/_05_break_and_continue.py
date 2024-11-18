number: int = 6
while True:
    number -= 1
    if number == 2:
        print("...Skipping 2...")
        continue
    elif number == 0:
        break
    else:
        print(number)
print("Done")
