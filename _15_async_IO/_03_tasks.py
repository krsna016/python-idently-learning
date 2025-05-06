import asyncio
from asyncio import Task
from datetime import datetime


async def fetch_data(input_data: int, *, delay: int) -> dict:
    print("Fetching Data...")
    start_time: datetime = datetime.now()
    await asyncio.sleep(delay)
    end_time: datetime = datetime.now()
    print("Data Retrived...")

    return {'input': input_data,
            'start_time': f'{start_time:%H:%M:%S}',
            'end_time': f'{end_time:%H:%M:%S}'}


async def main() -> None:
    task: Task[dict] = asyncio.create_task(fetch_data(3, delay=30))
    try:
        data: dict = await asyncio.wait_for(task, timeout=3)
        print(data)
    except asyncio.TimeoutError as e:
        print("Request took too long...")


if __name__ == '__main__':
    asyncio.run(main())
