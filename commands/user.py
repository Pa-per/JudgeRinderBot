"""User Cog for the bot."""

import discord
from discord.ext import commands

from utils.checks import is_cmd_channel
from utils.create import create_embed


class UserInfo(commands.Cog):
    """
    UserInfo The UserInfo class for the bot.

    Args:
        commands: The discord module for the bot.
    """

    def __init__(self, client):
        """
        __init__ Initialise the class.

        Args:
            client: The client the bot is using.
        """
        self.client = client

    @commands.command(
        name='avatar',
        description='Get information about a user.',
        aliases=['av'],
        usage='<user>',
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar(self, ctx, user: discord.Member = None):
        """
        Get a users avatar.

        Arguments:
            ctx: The context of the command.
            user: The user to get the avatar of.

        Keyword Arguments:
            user: The user to pass to the bot. (default: {None})
        """
        if is_cmd_channel(ctx):
            async with ctx.typing():
                if user is None:
                    user = ctx.author
                embed = create_embed(
                    description=f"{user.mention}\'s Avatar",
                    image=user.avatar.url,
                )
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(
        name='banner',
        description='Get a users banner',
        usage='<user>',
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def banner(self, ctx, user: discord.Member = None):
        """
        Get a users banner.

        Args:
            ctx: The context of the command.
            user: The user to get the banner of.

        Keyword Arguments:
            user: The user to pass to the bot. (default: {None})
        """
        if is_cmd_channel(ctx):
            async with ctx.typing():
                if user is None:
                    user = ctx.author
                user = await self.client.fetch_user(user.id)
                if user.banner:
                    embed = create_embed(
                        description=f"{user.mention}\'s Banner",
                        image=user.banner.url,
                    )
                    await ctx.reply(embed=embed, mention_author=False)
                else:
                    await ctx.reply(
                        f'{user.mention} has no banner.',
                        mention_author=False,
                    )
            return


async def setup(client: commands.Bot):
    """
    Create a new cog for the bot.

    Args:
        client (commands.Bot): The discord client.
    """
    await client.add_cog(UserInfo(client))
