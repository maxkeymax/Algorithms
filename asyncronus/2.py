'''
Write a Python program that creates three asynchronous functions and displays
their respective names with different delays (1 second, 2 seconds, and 3 seconds).
'''

import asyncio
from time import perf_counter


async def func1():
    print(f'{func1.__name__} started')
    await asyncio.sleep(1)
    print(f'{func1.__name__} ended')
    

async def func2():
    print(f'{func2.__name__} started')
    await asyncio.sleep(2)
    print(f'{func2.__name__} ended')
    
    
async def func3():
    print(f'{func3.__name__} started')
    await asyncio.sleep(3)
    print(f'{func3.__name__} ended')
    
    
async def main():
       
    start = perf_counter()
    await asyncio.gather(func1(), func2(), func3())
    print(perf_counter() - start)

if __name__ == '__main__':
    asyncio.run(main())