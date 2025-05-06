# asyncio is a Python library for writing asynchronous code.
# It allows you to run multiple tasks concurrently without blocking the program.
# This is useful for tasks like waiting for network responses or file I/O.


import asyncio


# Define an asynchronous function f1
async def f1(delay: int) -> None:
    print(f"f1 started with {delay} second delay")
    await asyncio.sleep(delay)  # Simulates a delay
    print("f1 finished")


# Define an asynchronous function f2
async def f2(delay: int) -> None:
    print(f"f2 started with {delay} second delay")
    await asyncio.sleep(delay)  # Simulates a delay
    print("f2 finished")


async def main() -> None:
    await asyncio.gather(f1(1), f2(2))


if __name__ == '__main__':
    asyncio.run(main())

"""
f1 and f2 are asynchronous functions with different delays.
asyncio.gather runs both functions concurrently.
Total time taken is the maximum delay (2 seconds), not the sum of delays (3 seconds) because both runs simultaneously.
"""
