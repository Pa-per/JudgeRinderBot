"""The Profile Cog."""

import discord
from discord.ext import commands

from utils.checks import is_cmd_channel
from utils.create import profile_embed
from utils.db import get_profile


class Profile(commands.Cog):
    """
    Define the Profile Class.

    Args:
        commands (_type_): The module to use from Discord.py.
    """

    def __init__(self, client):
        """
        Initialise the class.

        Args:
            client (_type_): The discord client.
        """
        self.client = client

    @commands.command(
        name='profile',
        description='Get a players courthouse profile.',
        usage='<user>',
    )
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def profile(self, ctx, user: discord.Member = None):
        """
        Search for a player's profile.

        Args:
            ctx (_type_): The command context to pull from.
            user (discord.Member, optional): The user to search for.
        """
        if is_cmd_channel(ctx):
            if user is None:
                user = ctx.author
            if user.bot:
                return
            msg = await ctx.send('Loading...')
            profile = await get_profile(user.id)
            embed = profile_embed(ctx.author, user, profile)
            await msg.edit(content='', embed=embed)


async def setup(client: commands.Bot):
    """
    Initialise the Profile Cog in the bot.

    Args:
        client (commands.Bot): The discord client.
    """
    await client.add_cog(Profile(client))
