import json

import discord
from discord.ext import commands

from utils.db import create_db
from utils.functions import load_cogs

intents = discord.Intents.all()

with open("config.json", encoding="utf-8") as config_file:
    config_file_data = json.load(config_file)
    token = config_file_data["bot"]["token"]


client = commands.Bot(command_prefix="-", intents=intents)


@client.event
async def on_ready():
    """
    on_ready When the bot is initialized these functions/events are ran.
    """
    await load_cogs(client)
    await create_db()
    await client.change_presence(
        activity=discord.Game(name="Objection Hearsay"),
        status=discord.Status.dnd
    )
    print("Bot is ready!")


client.run(token)
