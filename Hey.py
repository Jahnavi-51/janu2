import asyncio

async def Hello():
    print("HI!!!!!!")
    await asyncio.sleep(5)
    print("Hello!!!!")
async def run_Hello():
    await Hello()
    print("Hey!!!!")
asyncio.run(run_Hello())

def what():
    print("Janu")

def Why():
    print("Vasu")
    what()
Why()