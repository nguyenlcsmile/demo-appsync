
import asyncio


async def add(x, y):
    return x + y


async def get_results():
    res1 = await add(3, 4)
    res2 = await add(8, 5)

    print(res1, res2)

asyncio.run(get_results())
