'''
Write a Python program that implements a timeout for an asynchronous operation 
using asyncio.wait_for().

'''


import asyncio


async def worker():
    print('Start worker...')
    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        print('Process was cancelled!')
        raise
        
    
async def main():
    try:
        result = await asyncio.wait_for(worker(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print('Cancelled!')
        

if __name__ == '__main__':
    asyncio.run(main())