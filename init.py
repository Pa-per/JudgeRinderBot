"""JSON module to read from the configuration file."""
import json
import logging

import discord
from discord.ext import commands

from utils.db import create_db
from utils.functions import load_cogs

intents = discord.Intents.all()

logger = logging.getLogger('discord')
logging.basicConfig(filename='discord.log', encoding='utf-8', format="%(asctime)s %(message)s", datefmt="[%d-%m-%Y %H:%M:%S %p]: ")

with open('config.json', encoding='utf-8') as config_file:
    config_file_data = json.load(config_file)
    token = config_file_data['bot']['token']


client = commands.Bot(command_prefix='-', intents=intents)


@client.event
async def on_ready():
    """on_ready: When the bot is initialized these functions/events are ran."""
    await load_cogs(client)
    await create_db()
    await client.change_presence(
        activity=discord.Game(name='Objection Hearsay'),
        status=discord.Status.dnd,
    )
    logging.error(f'{client.user} has connected to Discord!')


client.run(token)
