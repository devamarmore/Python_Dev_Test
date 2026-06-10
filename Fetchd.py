import asyncio , aiohttp

async def fetch (session, url):
    async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.json()

async def fectch_both():
    url1 = ""
    url2 = ""

    async with aiohttp.ClientSession() as session:
        post, user = await asyncio.gather(fetch(session, url1), fetch(session, url2),)
    print("post:", post["title"]) 
    print("User:", user["name"])

asyncio.run(fectch_both())