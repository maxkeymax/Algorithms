'''
Write a Python program that implements a coroutine to fetch data from two
different URLs simultaneously using the "aiohttp" library.

'''


import asyncio
import aiohttp


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            
            if response.status == 200:
                print(f'{url} response status: {response.status}')
            else:
                raise Exception(f"Ошибка {response.status}")
            
async def main():
    urls = ['https://google.com', 'https://ya.ru']
    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
    
    await asyncio.gather(*tasks)
    

if __name__ == '__main__':
    asyncio.run(main())
    