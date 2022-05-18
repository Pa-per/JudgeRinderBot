"""Utility Commands."""

from discord.ext import commands
from utils.checks import is_cmd_channel
from utils.create import create_embed


class Ping(commands.Cog):
    """
    Ping Class.

    Args:
        commands (_type_): The discord commands module.
    """

    def __init__(self, client):
        """
        __init__ Initialise the class.

        Args:
            client (_type_): The discord client.
        """
        self.client = client

    @commands.command(
        name='ping',
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        """
        Get the bot's latency.

        Args:
            ctx (_type_): The command context to pull from.
        """
        if is_cmd_channel(ctx):
            async with ctx.typing():
                embed = create_embed(
                    title='Current Ping',
                    description=f'`{self.client.ws.latency * 1000:.0f}`ms',
                )
                embed.set_footer(
                    text=f'Requested by {ctx.author}',
                    icon_url=ctx.author.avatar.url,
                )
            await ctx.reply(embed=embed, mention_author=False)


async def setup(client: commands.Bot):
    """
    Initialise the Ping Cog in the bot.

    Args:
        client (commands.Bot): The discord client.
    """
    await client.add_cog(Ping(client))
