"""
Write a Python program that creates an asynchronous function to print
"Python Exercises!" with a two second delay.
"""

import asyncio


async def my_func():
    await asyncio.sleep(2)
    print("Python Exercises!")


async def main():
    await my_func()


if __name__ == "__main__":
    asyncio.run(main())
