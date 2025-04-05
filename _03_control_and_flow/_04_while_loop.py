import time

i = 1
while True:
    """
    This while loop increments `i` and prints its value until `i` equals 1000.
    """
    if i == 1000:
        break
    print(i)
    i += 1

connected: bool = True
while connected:
    """
    This while loop prints "Using Internet..." every 5 seconds and sets
    `connected` to False after the first iteration, ending the loop.
    """
    print("Using Internet...")
    time.sleep(5)
    connected = False
print("Connection ended...")
