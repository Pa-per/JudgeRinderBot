"""Event listener functions for the bot."""


import random
import time

import discord

from utils.db import add_exp, create_profile, get_level


class OnMessage(discord.ext.commands.Cog):
    """Class to specify that this class is a cog."""

    def __init__(self, client):
        """
        __init__ Initialise the class.

        Args:
            client: The client the bot is using.
        """
        self.client = client
        self.xp_cooldown = 0
        self.cooldown_members = {}

    @discord.ext.commands.Cog.listener()
    async def on_message(self, message):
        """
        on_message The event the bot will listen to.

        Args:
            message: The message the bot will use to gather data from.
        """
        member_cooldown = self.cooldown_members.setdefault(
            message.author.id, 0,
        )
        if message.author.bot:
            return
        if message.guild is None:
            return
        check = await self.client.get_context(message)
        if check.valid:
            return

        if time.time() - member_cooldown < self.xp_cooldown:
            return
        await create_profile(message.author.id)
        message_xp = random.randint(1, 9)
        levelled = await add_exp(message.author.id, message_xp)
        self.cooldown_members[message.author.id] = time.time()
        if levelled:
            level_up_channel_id = 973399767260471358
            channel = self.client.get_channel(level_up_channel_id)
            level = await get_level(message.author.id)
            msg = f'{message.author.mention} has reached level **{level}**!'
            await channel.send(msg)


async def setup(client: discord.ext.commands.Bot):
    """
    Create a new cog instance within the client.

    Args:
        client: the discord client
    """
    await client.add_cog(OnMessage(client))
