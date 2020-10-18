#async and await
import asyncio #this module has both asyn and await

async def main(): #excuted the function asynchronously
    print('Hello')
    await asyncio.sleep(3) #then the next line is executed after 3 seconds
    print('World')

asyncio.run(main())