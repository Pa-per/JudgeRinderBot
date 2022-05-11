import discord
from discord.ext import commands

from utils.checks import is_cmd_channel
from utils.create import create_embed


class Ping(commands.Cog):
    """The Bot Ping command."""

    def __init__(self, client):
        self.client = client

    @commands.command(name="ping", usage="")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        """Displays Judge Rinders current Ping."""
        if is_cmd_channel(ctx):
            async with ctx.typing():
                embed = create_embed(
                    title="Current Ping",
                    description=f"`{self.client.ws.latency * 1000:.0f}`ms",
                    color=discord.Color.green(),
                    footer=[f"Requested by {ctx.author}", f"{ctx.author.avatar.url}"],
                )
            await ctx.reply(embed=embed, mention_author=False)
        return


async def setup(client: commands.Bot):
    await client.add_cog(Ping(client))
