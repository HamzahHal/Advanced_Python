import asyncio
from roblox import Client

client = Client()


async def main():
    await client.get_user(1)


asyncio.get_event_loop().run_until_complete(main())