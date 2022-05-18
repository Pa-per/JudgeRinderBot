"""Music Cog."""

import discord
from discord.ext import commands


class Music(commands.Cog):
    """Music Cog."""

    def __init__(self, client):
        """
        __init__ Initialize the Music Class.

        Args:
            client (_type_): The discord client.
        """
        self.client = client

    @commands.command(name='play')
    async def play(self, ctx):
        """
        Join the users voice channel.

        Args:
            ctx (_type_): The Person invoking the command.
        """
        if ctx.author.voice.channel:
            channel = ctx.author.voice.channel
            voice = await channel.connect()
            await voice.play(
                discord.FFmpegPCMAudio(
                    'https://media-ssl.musicradio.com/HeartUK',
                ),
            )


async def setup(client: commands.Bot):
    """
    Initialise Music Cog.

    Args:
        client (commands.Bot): The discord client.
    """
    await client.add_cog(Music(commands.Bot))
