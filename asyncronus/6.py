"""
Write a Python program to create a coroutine that simulates a time-consuming
task and use asyncio.CancelledError to handle task cancellation.

"""

import asyncio


async def worker():
    print("Start worker...")
    try:
        await asyncio.sleep(3)
        print("Worker ws stoped")
    except asyncio.CancelledError:
        print("Process was cancelled!")
        raise


async def main():
    shelded = asyncio.create_task(worker())
    await asyncio.sleep(2)
    shelded.cancel()

    try:
        await shelded
    except asyncio.CancelledError:
        print("Canceled by sheld")


if __name__ == "__main__":
    asyncio.run(main())
