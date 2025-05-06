import asyncio
from asyncio import Future
from datetime import datetime

import requests
from requests import Response


async def check_status(url: str) -> dict[str, int | str]:
    start_time: datetime = datetime.now()
    response: Response = await asyncio.to_thread(requests.get, url, None)
    end_time: datetime = datetime.now()

    return {
        'website': url,
        'status': response.status_code,
        'start_time': f'{start_time:%H:%M:%S}',
        'end_time': f'{end_time:%H:%M:%S}'
    }


async def main() -> None:
    print("Fetching results...")
    tasks: Future = asyncio.gather(
        check_status("https://www.google.com"),
        check_status("https://www.github.com"),
        check_status("https://www.python.org"),
        check_status("https://www.stackoverflow.com"),
        check_status("https://lol"),
        return_exceptions=True
    )
    results: list[dict] = await tasks
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
