import random
import time
import discord

from utils.db import add_exp, create_profile, get_level


class OnMessage(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
        self.xp_cooldown=0
        self.cooldown_members = {}

    @discord.ext.commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.guild is None:
            return
        check = await self.client.get_context(message)
        if check.valid:
            return
        member_cooldown = self.cooldown_members.setdefault(message.author.id, 0)

        if time.time() - member_cooldown < self.xp_cooldown:
            return
        await create_profile(message.author.id)
        message_xp = random.randint(1, 9)
        levelled = await add_exp(message.author.id, message_xp)
        self.cooldown_members[message.author.id] = time.time()
        if levelled:
            channel = self.client.get_channel(973399767260471358)
            level = await get_level(message.author.id)
            message = f"{message.author.mention} has reached level **{level}**!"
            await channel.send(message)

async def setup(client: discord.ext.commands.Bot):
    await client.add_cog(OnMessage(client))