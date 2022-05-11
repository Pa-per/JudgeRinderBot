import os


async def load_cogs(client):
    for filename in os.listdir("commands"):
        if filename.endswith(".py"):
            await client.load_extension(f"commands.{filename[:-3]}")
            print(f"Loaded {filename[:-3]}")
    for filename in os.listdir("events"):
        if filename.endswith(".py"):
            await client.load_extension(f"events.{filename[:-3]}")
            print(f"Loaded {filename[:-3]}")
