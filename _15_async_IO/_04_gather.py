import asyncio
from asyncio import Future
from collections.abc import coroutine
from datetime import datetime


async def fetch_data(input_data: int, *, delay: int, fails: bool) -> dict:
    print("Fetching Data...")
    start_time: datetime = datetime.now()
    await asyncio.sleep(delay)
    end_time: datetime = datetime.now()

    if fails == True:
        raise Exception("Something bad happened!!")

    print("Data Retrived...")

    return {'input': input_data,
            'start_time': f'{start_time:%H:%M:%S}',
            'end_time': f'{end_time:%H:%M:%S}'}


async def main() -> None:
    task: Future = asyncio.gather(
        fetch_data(1, delay=1, fails=False),
        fetch_data(2, delay=2, fails=False),
        fetch_data(3, delay=1, fails=True),
        return_exceptions=True
    )

    results: list[dict] = await task
    print(results)


if __name__ == '__main__':
    asyncio.run(main())
