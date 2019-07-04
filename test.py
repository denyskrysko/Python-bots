import datetime
import asyncio


async def test():
    test = input("set up the time: ")
    ts = datetime.datetime.strptime(test, '%d-%m-%y %H:%M')
    print(ts - datetime.timedelta(minutes=15))
    await asyncio.sleep(ts)

asyncio.run(test())
