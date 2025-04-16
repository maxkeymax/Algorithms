"""
Write a Python program that creates an asyncio event loop and runs a coroutine
that prints numbers from 1 to 7 with a delay of 1 second each.

"""

import asyncio


async def display_numbers():
    for i in range(1, 8):
        print(i)
        await asyncio.sleep(1)


async def main():
    task = asyncio.create_task(display_numbers())

    await task


if __name__ == "__main__":
    asyncio.run(main())
