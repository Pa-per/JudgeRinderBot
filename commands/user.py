import discord
from discord.ext import commands
from utils.checks import is_cmd_channel

from utils.create import create_embed


class UserInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        name="avatar",
        description="Get information about a user.",
        aliases=["av"],
        usage="<user>"
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar(self, ctx, user: discord.Member = None):
        """Get a users avatar."""
        if is_cmd_channel(ctx):
            async with ctx.typing():
                if user is None:
                    user = ctx.author
                embed = create_embed(
                    description=f"{user.mention}'s Avatar",
                    image=user.avatar.url,
                    color=discord.Color.dark_theme()
                )
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        name="banner",
        description="Get a users banner",
        usage="<user>"
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def banner(self, ctx, user: discord.Member = None):
        """Get a users banner."""
        if is_cmd_channel(ctx):
            async with ctx.typing():
                if user is None:
                    user = ctx.author
                user = await self.client.fetch_user(user.id)
                if user.banner:
                    embed = create_embed(
                        description=f"{user.mention}'s Banner",
                        color=discord.Color.dark_theme(),
                        image=user.banner.url
                    )
                    await ctx.reply(embed=embed, mention_author=False)
                else:
                    await ctx.reply(f"{user.mention} has no banner.", mention_author=False)
            return


async def setup(client: commands.Bot):
    await client.add_cog(UserInfo(client))
