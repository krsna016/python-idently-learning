import time


# def func() -> None:
#     print("Recursion")
#     func()
# func()


def connecting_internet(signal: bool, delay: int) -> None:
    if delay > 5:
        signal = True
    if signal:
        print("Connected !")
    else:
        print(f"Connection failed...Try again in : {delay}'s...")
        time.sleep(delay)
        connecting_internet(signal, delay + 2)


connecting_internet(False, 1)
