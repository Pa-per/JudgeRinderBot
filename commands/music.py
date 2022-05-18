"""Music Cog."""


import contextlib

import discord
from discord.ext import commands
from utils.create import create_embed
from utils.functions import heart_now_playing


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
            with contextlib.suppress(TypeError):
                await voice.play(
                    discord.FFmpegPCMAudio(
                        'https://media-ssl.musicradio.com/HeartUK',
                    ),
                )

    @commands.command(
        name='nowplaying',
        description='Get the current song playing.',
        aliases=['np', 'currentsong', 'current'],
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def np(self, ctx):
        """
        Get the current song playing.

        Args:
            ctx (_type_): The Person invoking the command.
        """
        radio_name, radio_image, song_img = await heart_now_playing(self.client)
        embed = create_embed(
            title='Now Playing',
            author=[
                f'{radio_name}',
                f'{radio_image}',
            ],
            thumbnail=f'{song_img}',
        )
        await ctx.reply(embed=embed)


async def setup(client: commands.Bot):
    """
    Initialise Music Cog.

    Args:
        client (commands.Bot): The discord client.
    """
    await client.add_cog(Music(commands.Bot))
