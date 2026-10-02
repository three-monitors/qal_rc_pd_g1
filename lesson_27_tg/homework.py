import asyncio
import aiohttp
from datetime import datetime

# Клас для практики асинхронності


class AsyncWorker:
    def __init__(self, name):
        self.name = name

    async def work(self, duration):
        """Асинхронна робота з затримкою"""
        print(f"{self.name} почав працювати")
        await asyncio.sleep(duration)
        print(f"{self.name} завершив роботу за {duration} сек")
        return f"{self.name} виконав задачу"


async def main():
    """Головна асинхронна функція"""
    print("=== Асинхронне виконання ===")

    # Створення кількох задач
    workers = [
        AsyncWorker("Воркер A"),
        AsyncWorker("Воркер B"),
        AsyncWorker("Воркер C")
    ]

    # Паралельне виконання
    results = await asyncio.gather(
        workers[0].work(2),
        workers[1].work(1),
        workers[2].work(3)
    )

    print("\n=== Результати ===")
    for result in results:
        print(result)


async def fetch_url(url):
    """Асинхронний HTTP запит"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return f"{url}: {response.status}"


async def test_async_http():
    """Тест асинхронних HTTP запитів"""
    print("\n=== Асинхронні HTTP запити ===")

    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/uuid",
        "https://httpbin.org/delay/1"
    ]

    results = await asyncio.gather(
        *[fetch_url(url) for url in urls]
    )

    for result in results:
        print(result)

if __name__ == "__main__":
    # Запуск асинхронних функцій
    asyncio.run(main())
    asyncio.run(test_async_http())
