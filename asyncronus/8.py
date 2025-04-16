'''
Write a Python program that uses asyncio queues to simulate a producer-consumer
scenario with multiple producers and a single consumer.

'''


import asyncio
import random


async def producer(queue, id):
    item = f'Poducer {id} put {random.randint(0, 10)}'
    await queue.put(item)
    print(item)
    await asyncio.sleep(random.randint(1, 4))
    
    
async def consumer(queue):
    while True:
        item = await queue.get()
        print(f'***Consumer processed {item}***')
        queue.task_done()
        await asyncio.sleep(random.randint(1, 4))
        

async def main():
    queue = asyncio.Queue(maxsize=4)
    producer_tasks = [asyncio.create_task(producer(queue, i)) for i in range(4)]
    consumer_task = asyncio.create_task(consumer(queue))
    
    await asyncio.gather(*producer_tasks)
    await queue.join()
    consumer_task.cancel()


if __name__ == '__main__':
    asyncio.run(main())