import json

import discord
from discord.ext import commands
from utils.db import create_db

from utils.functions import load_cogs

intents = discord.Intents.all()

with open("config.json", encoding="utf-8") as file:
    data = json.load(file)
    token = data["bot"]["token"]

# initiate a discord bot class
client = commands.Bot(command_prefix="-", intents=intents)


@client.event
async def on_ready():
    await load_cogs(client)
    await create_db()
    print("Bot is ready!")

client.run(token)
